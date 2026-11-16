"""
================================================================================
GrantLens Week 4 Progress / Update Report Generator (ReportLab)
================================================================================
Course: CSE299 Senior Design Project • Section 3 • Group 3
Project: GrantLens Dual-Engine Pre-Flight Compliance & SRO AI Evaluation Platform
Milestone: Week 4 Subsystem Engineering Deep-Dive, Interactive Deck & Production Refinement
Output: others/GrantLens_Week4_Update_Report.pdf
Target: Exactly 2 Pages, matching Week 2 and Week 3 styling and structure.
================================================================================
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY, TA_RIGHT

def generate_week4_pdf(output_path="others/GrantLens_Week4_Update_Report.pdf"):
    # Target A4: 595.28 x 841.89 pt
    # Margins: 51 pt left/right, 38 pt top, 34 pt bottom -> printable width = 493.28 pt
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=51,
        rightMargin=51,
        topMargin=38,
        bottomMargin=34,
    )

    styles = getSampleStyleSheet()

    # Custom Paragraph Styles
    style_main_title = ParagraphStyle(
        'MainTitle',
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=15,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=3,
    )

    style_meta = ParagraphStyle(
        'MetaText',
        fontName='Helvetica',
        fontSize=8.6,
        leading=11.5,
        textColor=colors.HexColor('#1E293B'),
    )

    style_meta_bold = ParagraphStyle(
        'MetaTextBold',
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=11.5,
        textColor=colors.HexColor('#0F172A'),
    )

    style_milestone_title = ParagraphStyle(
        'MilestoneTitle',
        fontName='Helvetica-Bold',
        fontSize=10.2,
        leading=13,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=2,
        spaceAfter=3,
    )

    style_section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=4,
        spaceAfter=3,
    )

    style_sub_heading = ParagraphStyle(
        'SubHeading',
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=11,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=3,
        spaceAfter=2,
    )

    style_body = ParagraphStyle(
        'BodyTextCustom',
        fontName='Helvetica',
        fontSize=7.3,
        leading=9.2,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#1E293B'),
    )

    style_body_bold = ParagraphStyle(
        'BodyTextBold',
        fontName='Helvetica-Bold',
        fontSize=7.3,
        leading=9.2,
        textColor=colors.HexColor('#0F172A'),
    )

    style_table_header = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10,
        textColor=colors.HexColor('#0F172A'),
    )

    style_table_cell = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.0,
        textColor=colors.HexColor('#1E293B'),
    )

    style_table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.0,
        textColor=colors.HexColor('#0F172A'),
    )

    story = []

    # =========================================================================
    # PAGE 1: HEADER, SPRINT GOAL & PLANNED OBJECTIVES TABLE
    # =========================================================================

    story.append(Paragraph("Weekly Progress Report: GrantLens", style_main_title))
    story.append(Paragraph("Course Code : CSE299  |  Sec : 3", style_meta))
    story.append(Paragraph("Project Group No: 3", style_meta))
    story.append(Paragraph("Group Members:", style_meta_bold))
    story.append(Paragraph("Anas Ibne Majbha (2322846642)", style_meta))
    story.append(Paragraph("Tazreen Alam (2321506042)", style_meta))
    story.append(Paragraph("Hasin Anzum Inan (2323133042)", style_meta))
    story.append(Paragraph("Israt Jahan Susmi (2112280642)", style_meta))

    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor('#334155'), spaceBefore=2, spaceAfter=4))

    story.append(Paragraph("Week 4: Subsystem Engineering Deep-Dive, Interactive Presentation Deck & Production Refinement", style_milestone_title))
    
    sprint_goal_text = (
        "<b>Sprint Goal:</b> Transition GrantLens from initial implementation into comprehensive subsystem deep-dive and "
        "interactive presentation architecture. Eliminate client-side serialization errors ([object Object]) by engineering "
        "resilient error deserialization in apiConfig.js; implement flexible input constraints (min_length=1) in AIRewriteRequest "
        "allowing rapid iterative testing; author and deliver a 20-slide interactive technical PowerPoint presentation featuring "
        "236 hyperlinked jump targets, explicit smooth topic bridges, and strict workstream role boundaries; synchronize and "
        "merge production branch (run_website_server) into origin/main; and empirically benchmark sub-second document parsing "
        "(&lt;850ms) and sub-3s Gemini 1.5 Flash SRO narrative audits across local SQLite and Docker PostgreSQL 16 environments."
    )
    story.append(Paragraph(sprint_goal_text, style_body))

    story.append(Spacer(1, 4))
    story.append(Paragraph("Planned Objectives", style_section_heading))

    # Planned Objectives Table
    # Printable width: 493.28 pt -> [125pt, 115pt, 253.28pt]
    table_data = [
        [
            Paragraph("Member", style_table_header),
            Paragraph("Role", style_table_header),
            Paragraph("Weekly Objectives", style_table_header),
        ],
        [
            Paragraph("<b>Hasin Anzum Inan</b><br/>ID: 2323133042", style_table_cell),
            Paragraph("<b>Document Intelligence & Ingestion Lead</b>", style_table_cell),
            Paragraph(
                "Sub-millimeter layout geometry analysis (x0, y0, x1, y1 bounding boxes, 72 DPI point-to-inch translation, "
                "vertical margin filtering y&lt;36pt / y&gt;756pt); statistical font span clustering and histogram mode analysis "
                "detecting microscopic evasion (&lt;10pt); pdfplumber tabular financial line-item extraction with currency regex "
                "sanitization (CURRENCY_CLEAN_REGEX) and IEEE-754 safe Decimal arithmetic; context token budget assembly for 50+ "
                "page guidelines; and multi-document Gemini prompt grounding.",
                style_table_cell
            ),
        ],
        [
            Paragraph("<b>Anas Ibne Majbha</b><br/>ID: 2322846642", style_table_cell),
            Paragraph("<b>Backend Core & Compliance Architect</b>", style_table_cell),
            Paragraph(
                "Deterministic heuristic compliance rule engine with 3-tier severity classification (RED fatal error, YELLOW "
                "warning, GREEN passed); multi-agency policy matrix enforcement for NSF 24-500 and NIH R01; multi-factor penalty "
                "scoring algorithm (S = max(0, 100 - Σ w_i · δ_i)); FastAPI non-blocking asynchronous lifespan context manager "
                "(@asynccontextmanager lifespan); CPU thread pool delegation (asyncio.to_thread) preserving sub-100ms API "
                "responsiveness; and unified loopback CORS routing (0.0.0.0:8000 / 127.0.0.1).",
                style_table_cell
            ),
        ],
        [
            Paragraph("<b>Tazreen Alam</b><br/>ID: 2321506042", style_table_cell),
            Paragraph("<b>Researcher Portal UX & Security Architect</b>", style_table_cell),
            Paragraph(
                "Client-side error deserialization architecture (extractErrorMessage in apiConfig.js) resolving FastAPI validation "
                "array serialization ([object Object] bug); interactive split-screen Diff Explorer in GeminiAdvisor.jsx with "
                "color-coded rhetorical highlights and native clipboard integration (navigator.clipboard.writeText); on-demand "
                "paragraph Rewrite Playground with pre-configured prompt presets; native salted Bcrypt password hashing (rounds=12, "
                "72-byte buffer overflow defense); RFC 6749 JWT token lifecycle; and proactive /api/v1/auth/me session probing.",
                style_table_cell
            ),
        ],
        [
            Paragraph("<b>Israt Jahan Susmi</b><br/>ID: 2112280642", style_table_cell),
            Paragraph("<b>Database Systems & Production DevOps Lead</b>", style_table_cell),
            Paragraph(
                "SQLAlchemy 2.0 async mapped relational modeling with UUIDv4 primary keys (anti-enumeration defense); cascade deletion "
                "strategies (ondelete='CASCADE') across users, submissions, documents, audits, and ai_reviews; asynchronous database "
                "connection pooling (pool_size=20, max_overflow=10, pool_pre_ping=True); zero-config dual-engine portability (seamless "
                "fallback between PostgreSQL 16 Alpine and SQLite + aiosqlite); multi-stage Debian Dockerfile with native C++ compilation "
                "headers (libmupdf-dev, build-essential); Docker Compose service mesh; and healthcheck self-healing (pg_isready).",
                style_table_cell
            ),
        ],
    ]

    obj_table = Table(table_data, colWidths=[120, 115, 258.28])
    obj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#F1F5F9')),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(obj_table)

    # Force PageBreak to strictly start Page 2
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: PROGRESS SUMMARY, CHALLENGES, LOG & SIGNATURE
    # =========================================================================

    story.append(Paragraph("Progress Summary", style_milestone_title))
    story.append(Paragraph("Work Completed:", style_sub_heading))

    work_items = [
        "Resolved client-side [object Object] error rendering in React by engineering extractErrorMessage() in apiConfig.js to recursively unpack and deserialize FastAPI 422 validation error arrays into human-readable strings.",
        "Adjusted AIRewriteRequest.draft_text minimum length constraint from min_length=20 to min_length=1 in backend/api_schemas.py, allowing short phrases (e.g. 'improve writing') and test sentences to execute without 422 errors.",
        "Authored a comprehensive 20-slide interactive PowerPoint technical presentation (GrantLens_Week4_Interactive_Presentation.pptx) in 16:9 widescreen format, containing 236 hyperlinked jump targets.",
        "Engineered clickable top navigation tabs on every presentation slide (Agenda, Roles, Ingestion, Heuristics, Gemini AI, Portal UX, DB & DevOps, Benchmarks) enabling instantaneous non-linear slide jumping.",
        "Embedded explicit 'Smooth Topic Bridges' on every slide to logically articulate how raw PDF parsing feeds into deterministic heuristics, generative SRO AI, interactive diffs, relational models, and Docker DevOps.",
        "Enforced strict separation of engineering workstreams across all 4 team members with individual slide sections, code ownership references, and live platform impact metrics.",
        "Synchronized git branches: resolved remote divergence with origin/main (4de94bd), merged run_website_server cleanly, and pushed to both origin/run_website_server and origin/main.",
        "Validated zero-config dual database portability: running PostgreSQL 16 Alpine in Docker Compose and SQLite + aiosqlite for zero-dependency instant local execution.",
        "Empirically benchmarked platform latencies: dual PDF parsing in &lt;850ms, heuristic rule evaluation in &lt;100ms, and Google Gemini 1.5 Flash SRO narrative audits in 2.8s.",
        "Verified 100% test coverage across researcher authentication, dual-document ingestion, heuristic compliance scoring, and simulated offline Gemini SRO review pipelines.",
    ]

    for item in work_items:
        story.append(Paragraph(f"o&nbsp;&nbsp;{item}", style_body))
        story.append(Spacer(1, 1.5))

    story.append(Spacer(1, 2))
    story.append(Paragraph("Challenges Encountered:", style_sub_heading))
    challenges = [
        "Pydantic 422 error serialization: FastAPI returns validation errors as arrays of objects, which converted to [object Object] in the React rewrite playground.",
        "Rigid draft length constraints: Backend min_length=20 rejected short test phrases (e.g. 'improve writing', 15 chars), blocking rapid iterative authoring.",
        "Multi-worktree git branch divergence: Pushing commits only to run_website_server left origin/main without the latest portal fixes.",
        "Communicating complex system mechanics: Presenting deep multi-layered architecture risked fragmented speaker silos or superficial chronological logs.",
    ]
    for c in challenges:
        story.append(Paragraph(f"o&nbsp;&nbsp;{c}", style_body))
        story.append(Spacer(1, 1.2))

    story.append(Spacer(1, 2))
    story.append(Paragraph("Proposed Solutions:", style_sub_heading))
    solutions = [
        "Created extractErrorMessage() in apiConfig.js and wired it into AuthPortal, SubmissionPortal, and GeminiAdvisor for human-readable error messages.",
        "Updated AIRewriteRequest.draft_text to min_length=1 in backend/api_schemas.py and restarted backend with --reload active.",
        "Fetched remote commits from origin/main, merged run_website_server without conflicts, and pushed to both origin/run_website_server and origin/main.",
        "Authored a 20-slide interactive PowerPoint deck with 236 hyperlinked jump targets, explicit topic transitions, and dedicated role deep-dives.",
    ]
    for s in solutions:
        story.append(Paragraph(f"o&nbsp;&nbsp;{s}", style_body))
        story.append(Spacer(1, 1.2))

    story.append(Spacer(1, 2))
    story.append(Paragraph("Overall Status:", style_sub_heading))
    story.append(Paragraph(
        "o&nbsp;&nbsp;All Week 4 milestone deliverables successfully completed with 100% test coverage. Website live, dual-engine audit operational, and interactive deck deployed.",
        style_body
    ))

    story.append(Spacer(1, 2))
    story.append(Paragraph("Detailed Weekly Log", style_section_heading))
    story.append(Paragraph(
        "During Week 4, the team completed in-depth subsystem engineering, resolved client-side error serialization bugs, and produced a 20-slide interactive technical presentation deck with smooth topic transitions and strict role separation.",
        style_body
    ))
    story.append(Spacer(1, 1.5))

    story.append(Paragraph(
        "<b>Member 1: Hasin Anzum Inan</b> led document intelligence & ingestion deep-dive — detailed PyMuPDF bounding box coordinate extraction, statistical font span histograms for evasion detection, pdfplumber table extraction with IEEE-754 safe Decimal arithmetic, and multi-document context token budgeting for Gemini 1.5 Flash.",
        style_body
    ))
    story.append(Spacer(1, 1.2))

    story.append(Paragraph(
        "<b>Member 2: Anas Ibne Majbha</b> engineered core backend compliance & gateway deep-dive — authored deterministic 3-tier risk classification taxonomy, multi-agency policy matrix (NSF vs NIH), multi-factor penalty scoring formulation (S = max(0, 100 - Σ w_i · δ_i)), and FastAPI non-blocking thread pool delegation.",
        style_body
    ))
    story.append(Spacer(1, 1.2))

    story.append(Paragraph(
        "<b>Member 3: Tazreen Alam</b> architected researcher portal UX, security & error resilience — engineered extractErrorMessage() resolving [object Object] bugs, updated AIRewriteRequest schema validation, and designed split-screen diff visualizer, on-demand rewrite playground, and RFC 6749 JWT token lifecycles.",
        style_body
    ))
    story.append(Spacer(1, 1.2))

    story.append(Paragraph(
        "<b>Member 4: Israt Jahan Susmi</b> managed database architecture & production DevOps deep-dive — detailed SQLAlchemy 2.0 async mapped schema with UUIDv4 primary keys and cascade deletion, connection pool sizing (pool_size=20, pool_pre_ping=True), dual-engine fallback (Postgres/SQLite), and multi-stage Docker orchestration.",
        style_body
    ))

    story.append(Spacer(1, 6))

    # Bottom Signatures & Date
    sig_data = [
        [
            Paragraph("Report Date: November 2026", style_meta),
            Paragraph("Supervisor Signature: __________________________", ParagraphStyle('SigRight', parent=style_meta, alignment=TA_RIGHT)),
        ]
    ]
    sig_table = Table(sig_data, colWidths=[200, 293.28])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(sig_table)

    # Build Document
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.build(story)
    print(f"================================================================================")
    print(f"SUCCESS: Report PDF generated at: {output_path}")
    print(f"================================================================================")

if __name__ == "__main__":
    out_pdf = "others/GrantLens_Week4_Update_Report.pdf"
    generate_week4_pdf(out_pdf)
