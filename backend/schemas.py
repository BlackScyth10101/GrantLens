from decimal import Decimal
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class FontSpanMetric(BaseModel):
    font: str
    size: float
    flags: int
    is_bold: bool
    is_italic: bool
    text: str


class PageGeometry(BaseModel):
    page_number: int
    width_pt: float
    height_pt: float
    margin_top_in: float
    margin_bottom_in: float
    margin_left_in: float
    margin_right_in: float


class ParsedTableRecord(BaseModel):
    page_number: int
    headers: List[str]
    rows: List[List[str]]
    structured_records: List[Dict[str, Any]]


class ExtractedBudgetLine(BaseModel):
    category: str
    description: str
    amount: Decimal
    currency: str = "USD"
    page: int
    source_table_index: int


class DocumentIngestionResult(BaseModel):
    filename: str
    doc_type: str
    page_count: int
    dominant_font_name: str
    dominant_font_size: float
    min_font_size: float
    max_font_size: float
    min_margins: Dict[str, float]
    sections_detected: List[str]
    tables: List[ParsedTableRecord]
    budget_items: List[ExtractedBudgetLine]
    total_requested_budget: Decimal
    extracted_text_by_page: Dict[int, str]
