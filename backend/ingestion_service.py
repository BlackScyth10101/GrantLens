import asyncio
import io
import re
from collections import Counter
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List, Optional, Tuple
import fitz  # PyMuPDF
import pdfplumber
from schemas import (
    DocumentIngestionResult,
    ExtractedBudgetLine,
    FontSpanMetric,
    PageGeometry,
    ParsedTableRecord,
)

# Regex to match currency amounts: e.g. $12,450.00, 50000 USD, $ 100,000
CURRENCY_CLEAN_REGEX = re.compile(r"[^\d.-]")
BUDGET_KEYWORD_REGEX = re.compile(
    r"(budget|personnel|salary|fringe|equipment|travel|participant|supplies|direct|indirect|overhead|total|subaward|cost)",
    re.IGNORECASE,
)


class DocumentIngestionService:
    @staticmethod
    def _clean_numeric(value_str: Any) -> Optional[Decimal]:
        if not value_str:
            return None
        cleaned = CURRENCY_CLEAN_REGEX.sub("", str(value_str).strip())
        if not cleaned:
            return None
        try:
            return Decimal(cleaned)
        except InvalidOperation:
            return None

    @classmethod
    def _extract_pymupdf_geometry(
        cls,
        file_bytes: bytes,
    ) -> Tuple[int, str, float, float, float, Dict[str, float], List[str], Dict[int, str]]:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        page_count = len(doc)

        font_counts: Counter = Counter()
        font_sizes: List[float] = []
        min_top = 999.0
        min_bottom = 999.0
        min_left = 999.0
        min_right = 999.0

        sections_detected: List[str] = []
        extracted_text_by_page: Dict[int, str] = {}

        for page_idx in range(page_count):
            page = doc[page_idx]
            page_rect = page.rect  # width, height in 72 dpi points
            text_dict = page.get_text("dict")
            page_text_builder = []

            for block in text_dict.get("blocks", []):
                if block.get("type") == 0:  # text block
                    for line in block.get("lines", []):
                        line_text = ""
                        for span in line.get("spans", []):
                            text = span.get("text", "").strip()
                            if not text:
                                continue

                            font_name = span.get("font", "Unknown")
                            font_size = round(span.get("size", 10.0), 2)
                            font_counts[(font_name, font_size)] += len(text)
                            font_sizes.append(font_size)
                            line_text += " " + text

                            # Bounding box analysis for margins
                            bbox = span.get("bbox")  # (x0, y0, x1, y1)
                            if bbox:
                                # Convert points (72 pt = 1 in) to inches
                                top_margin_in = bbox[1] / 72.0
                                bottom_margin_in = (page_rect.height - bbox[3]) / 72.0
                                left_margin_in = bbox[0] / 72.0
                                right_margin_in = (page_rect.width - bbox[2]) / 72.0

                                if top_margin_in > 0:
                                    min_top = min(min_top, top_margin_in)
                                if bottom_margin_in > 0:
                                    min_bottom = min(min_bottom, bottom_margin_in)
                                if left_margin_in > 0:
                                    min_left = min(min_left, left_margin_in)
                                if right_margin_in > 0:
                                    min_right = min(min_right, right_margin_in)

                        cleaned_line = line_text.strip()
                        if cleaned_line:
                            page_text_builder.append(cleaned_line)
                            # Section heading heuristics (capitalized line, short, distinct)
                            if (
                                len(cleaned_line) < 80
                                and (cleaned_line.isupper() or cleaned_line.istitle())
                                and any(
                                    kw in cleaned_line.lower()
                                    for kw in [
                                        "abstract",
                                        "project description",
                                        "narrative",
                                        "references",
                                        "budget justification",
                                        "facilities",
                                        "equipment",
                                        "biosketch",
                                        "data management",
                                    ]
                                )
                            ):
                                sections_detected.append(cleaned_line)

            extracted_text_by_page[page_idx + 1] = "\n".join(page_text_builder)

        doc.close()

        dominant_font_name = "Times-Roman"
        dominant_font_size = 11.0
        if font_counts:
            (dominant_font_name, dominant_font_size), _ = font_counts.most_common(1)[0]

        min_font_size = min(font_sizes) if font_sizes else 11.0
        max_font_size = max(font_sizes) if font_sizes else 11.0

        min_margins = {
            "top_in": round(min_top if min_top != 999.0 else 1.0, 3),
            "bottom_in": round(min_bottom if min_bottom != 999.0 else 1.0, 3),
            "left_in": round(min_left if min_left != 999.0 else 1.0, 3),
            "right_in": round(min_right if min_right != 999.0 else 1.0, 3),
        }

        return (
            page_count,
            dominant_font_name,
            dominant_font_size,
            min_font_size,
            max_font_size,
            min_margins,
            list(dict.fromkeys(sections_detected)),
            extracted_text_by_page,
        )

    @classmethod
    def _extract_pdfplumber_tables(
        cls,
        file_bytes: bytes,
    ) -> Tuple[List[ParsedTableRecord], List[ExtractedBudgetLine], Decimal]:
        parsed_tables: List[ParsedTableRecord] = []
        budget_items: List[ExtractedBudgetLine] = []
        total_requested = Decimal("0.00")

        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page_idx, page in enumerate(pdf.pages):
                tables = page.extract_tables()
                for table_idx, raw_table in enumerate(tables):
                    if not raw_table or len(raw_table) < 2:
                        continue

                    headers = [
                        re.sub(r"\s+", " ", str(col or "")).strip()
                        for col in raw_table[0]
                    ]
                    rows: List[List[str]] = []
                    structured: List[Dict[str, Any]] = []

                    is_budget_table = any(
                        BUDGET_KEYWORD_REGEX.search(h) for h in headers
                    )

                    for raw_row in raw_table[1:]:
                        cleaned_row = [
                            re.sub(r"\s+", " ", str(cell or "")).strip()
                            for cell in raw_row
                        ]
                        if not any(cleaned_row):
                            continue
                        rows.append(cleaned_row)

                        row_dict = {}
                        for idx, h in enumerate(headers):
                            if idx < len(cleaned_row):
                                row_dict[h if h else f"col_{idx}"] = cleaned_row[idx]
                        structured.append(row_dict)

                        if is_budget_table:
                            desc = cleaned_row[0] if len(cleaned_row) > 0 else "Unknown"
                            numeric_candidates = [
                                cls._clean_numeric(cell) for cell in cleaned_row[1:]
                            ]
                            valid_nums = [n for n in numeric_candidates if n is not None]

                            if valid_nums:
                                line_amt = valid_nums[-1]  # Highest column usually total
                                if (
                                    "total" in desc.lower()
                                    and line_amt > total_requested
                                ):
                                    total_requested = line_amt
                                elif not "total" in desc.lower():
                                    budget_items.append(
                                        ExtractedBudgetLine(
                                            category=desc,
                                            description=desc,
                                            amount=line_amt,
                                            page=page_idx + 1,
                                            source_table_index=table_idx,
                                        )
                                    )

                    parsed_tables.append(
                        ParsedTableRecord(
                            page_number=page_idx + 1,
                            headers=headers,
                            rows=rows,
                            structured_records=structured,
                        )
                    )

        if total_requested == Decimal("0.00") and budget_items:
            total_requested = sum((item.amount for item in budget_items), Decimal("0.00"))

        return parsed_tables, budget_items, total_requested

    @classmethod
    async def process_pdf(
        cls,
        file_bytes: bytes,
        filename: str,
        doc_type: str,
    ) -> DocumentIngestionResult:
        # Run CPU-intensive PDF parsing in a managed thread pool
        geo_result = await asyncio.to_thread(
            cls._extract_pymupdf_geometry,
            file_bytes,
        )
        (
            page_count,
            dominant_font_name,
            dominant_font_size,
            min_font_size,
            max_font_size,
            min_margins,
            sections_detected,
            extracted_text_by_page,
        ) = geo_result

        tbl_result = await asyncio.to_thread(
            cls._extract_pdfplumber_tables,
            file_bytes,
        )
        parsed_tables, budget_items, total_requested = tbl_result

        return DocumentIngestionResult(
            filename=filename,
            doc_type=doc_type,
            page_count=page_count,
            dominant_font_name=dominant_font_name,
            dominant_font_size=dominant_font_size,
            min_font_size=min_font_size,
            max_font_size=max_font_size,
            min_margins=min_margins,
            sections_detected=sections_detected,
            tables=parsed_tables,
            budget_items=budget_items,
            total_requested_budget=total_requested,
            extracted_text_by_page=extracted_text_by_page,
        )
