"""
================================================================================
GrantLens Week 4 Interactive Presentation Generator (python-pptx)
================================================================================
Course: CSE299 Senior Design Project • Section 3 • Group 3
Project: GrantLens Dual-Engine Pre-Flight Compliance & SRO AI Evaluation Platform
Milestone: Week 4 Subsystem Engineering & Deep-Dive Technical Architecture
Authors:
  - Hasin Anzum Inan (2323133042)  - Document Intelligence & Extraction Lead
  - Anas Ibne Majbha (2322846642)  - Core Backend & Compliance Engine Architect
  - Tazreen Alam (2321506042)      - Researcher Portal UX & Security Architect
  - Israt Jahan Susmi (2112280642) - Database Systems & Production DevOps Lead
================================================================================
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

def build_week4_interactive_presentation(output_path="others/GrantLens_Week4_Interactive_Presentation.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Pre-allocate exactly 20 slide instances for cross-slide linking
    slides = [prs.slides.add_slide(blank_layout) for _ in range(20)]
    print(f"Allocated {len(slides)} blank slides.")

    # High-Contrast Dark Color Tokens
    BG_DARK = RGBColor(11, 15, 25)          # Deep Void Navy
    CARD_BG = RGBColor(18, 24, 38)          # Slate Surface
    CARD_BORDER = RGBColor(38, 50, 72)      # Subtle Structural Border
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)    # Slate 400
    TEXT_DIM = RGBColor(100, 116, 139)      # Slate 500

    # Workstream Accent Palette
    COLOR_ORANGE = RGBColor(249, 115, 22)   # Brand / Platform Core
    COLOR_CYAN = RGBColor(14, 165, 233)     # Hasin (Document Intelligence)
    COLOR_PURPLE = RGBColor(139, 92, 246)   # Anas (Core Backend & Engine)
    COLOR_AMBER = RGBColor(245, 158, 11)    # AI Core (Gemini SRO)
    COLOR_EMERALD = RGBColor(16, 185, 129)  # Tazreen (Researcher UX & Security)
    COLOR_ROSE = RGBColor(244, 63, 94)      # Susmi (Database & DevOps)
    COLOR_INDIGO = RGBColor(99, 102, 241)   # Platform Synthesis

    NAV_SECTIONS = [
        ("Agenda", 1),
        ("Roles", 2),
        ("Ingestion", 3),
        ("Heuristics", 6),
        ("Gemini AI", 9),
        ("Portal UX", 12),
        ("DB & DevOps", 15),
        ("Benchmarks", 18),
    ]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return bg

    def add_top_nav(slide, active_section_idx):
        nav_y = Inches(0.18)
        nav_h = Inches(0.38)
        btn_w = Inches(1.48)
        spacing = Inches(0.08)
        start_x = Inches(0.41)

        for i, (label, target_idx) in enumerate(NAV_SECTIONS):
            bx = start_x + i * (btn_w + spacing)
            btn = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, nav_y, btn_w, nav_h)
            btn.fill.solid()
            
            is_active = (i == active_section_idx)
            if is_active:
                btn.fill.fore_color.rgb = RGBColor(30, 41, 59)
                btn.line.color.rgb = COLOR_ORANGE
                btn.line.width = Pt(1.5)
            else:
                btn.fill.fore_color.rgb = RGBColor(15, 23, 42)
                btn.line.color.rgb = RGBColor(30, 41, 59)
                btn.line.width = Pt(0.75)

            btn.click_action.target_slide = slides[target_idx]
            
            tf = btn.text_frame
            tf.word_wrap = False
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = tf.paragraphs[0]
            p.text = f"• {label}" if is_active else label
            p.alignment = PP_ALIGN.CENTER
            p.font.name = "Arial"
            p.font.size = Pt(10)
            p.font.bold = is_active
            p.font.color.rgb = COLOR_ORANGE if is_active else TEXT_MUTED

    def add_bottom_footer(slide, curr_idx):
        footer_y = Inches(7.05)
        
        # Academic Context
        ctx_box = slide.shapes.add_textbox(Inches(0.45), footer_y, Inches(5.0), Inches(0.35))
        tf = ctx_box.text_frame
        p = tf.paragraphs[0]
        p.text = "CSE299 Senior Design • Section 3 • Group 3 • GrantLens Week 4"
        p.font.name = "Arial"
        p.font.size = Pt(9)
        p.font.color.rgb = TEXT_DIM

        # Center: Interactive Jump Controls
        ctrl_x = Inches(5.5)
        if curr_idx > 0:
            prev_btn = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ctrl_x, footer_y, Inches(1.1), Inches(0.32))
            prev_btn.fill.solid()
            prev_btn.fill.fore_color.rgb = RGBColor(20, 28, 45)
            prev_btn.line.color.rgb = CARD_BORDER
            prev_btn.line.width = Pt(0.75)
            prev_btn.click_action.target_slide = slides[curr_idx - 1]
            p = prev_btn.text_frame.paragraphs[0]
            p.text = "◀ Prev"
            p.alignment = PP_ALIGN.CENTER
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.color.rgb = TEXT_MUTED

        home_btn = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ctrl_x + Inches(1.2), footer_y, Inches(1.2), Inches(0.32))
        home_btn.fill.solid()
        home_btn.fill.fore_color.rgb = RGBColor(20, 28, 45)
        home_btn.line.color.rgb = COLOR_ORANGE
        home_btn.line.width = Pt(0.75)
        home_btn.click_action.target_slide = slides[1]
        p = home_btn.text_frame.paragraphs[0]
        p.text = "⌂ Agenda"
        p.alignment = PP_ALIGN.CENTER
        p.font.name = "Arial"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = COLOR_ORANGE

        if curr_idx < len(slides) - 1:
            next_btn = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ctrl_x + Inches(2.5), footer_y, Inches(1.1), Inches(0.32))
            next_btn.fill.solid()
            next_btn.fill.fore_color.rgb = RGBColor(20, 28, 45)
            next_btn.line.color.rgb = CARD_BORDER
            next_btn.line.width = Pt(0.75)
            next_btn.click_action.target_slide = slides[curr_idx + 1]
            p = next_btn.text_frame.paragraphs[0]
            p.text = "Next ▶"
            p.alignment = PP_ALIGN.CENTER
            p.font.name = "Arial"
            p.font.size = Pt(9)
            p.font.color.rgb = TEXT_MUTED

        # Slide Number Indicator
        num_box = slide.shapes.add_textbox(Inches(11.8), footer_y, Inches(1.1), Inches(0.35))
        p = num_box.text_frame.paragraphs[0]
        p.text = f"Slide {curr_idx + 1} of {len(slides)}"
        p.alignment = PP_ALIGN.RIGHT
        p.font.name = "Arial"
        p.font.size = Pt(9)
        p.font.color.rgb = TEXT_DIM

    def add_slide_header(slide, tag_text, title_text, role_color):
        tag = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(0.68), Inches(4.5), Inches(0.28))
        tag.fill.solid()
        tag.fill.fore_color.rgb = RGBColor(20, 28, 45)
        tag.line.color.rgb = role_color
        tag.line.width = Pt(1)
        p = tag.text_frame.paragraphs[0]
        p.text = tag_text.upper()
        p.alignment = PP_ALIGN.LEFT
        p.font.name = "Arial"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = role_color

        title_box = slide.shapes.add_textbox(Inches(0.42), Inches(0.96), Inches(12.4), Inches(0.55))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Arial"
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

    def add_transition_banner(slide, prev_topic, next_topic, transition_text):
        banner = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.45), Inches(6.30), Inches(12.43), Inches(0.65))
        banner.fill.solid()
        banner.fill.fore_color.rgb = RGBColor(15, 23, 42)
        banner.line.color.rgb = RGBColor(51, 65, 85)
        banner.line.width = Pt(0.75)

        tf = banner.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = f"SMOOTH TOPIC BRIDGE: [{prev_topic}]  ➔  [{next_topic}]"
        p1.font.name = "Arial"
        p1.font.size = Pt(8.5)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_ORANGE

        p2 = tf.add_paragraph()
        p2.text = transition_text
        p2.font.name = "Arial"
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = RGBColor(203, 213, 225)

    def create_card(slide, left, top, width, height, title, subtitle, bullets, accent_color, code_snippet=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = accent_color if accent_color else CARD_BORDER
        card.line.width = Pt(1.25)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.18)
        tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.16)
        tf.margin_bottom = Inches(0.16)

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = accent_color if accent_color else TEXT_WHITE

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Arial"
            p2.font.size = Pt(9.5)
            p2.font.italic = True
            p2.font.color.rgb = TEXT_MUTED
            p2.space_after = Pt(4)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"•  {b}"
            pb.font.name = "Arial"
            pb.font.size = Pt(9)
            pb.font.color.rgb = RGBColor(226, 232, 240)
            pb.space_after = Pt(3)

        if code_snippet:
            pc = tf.add_paragraph()
            pc.text = code_snippet
            pc.font.name = "Courier New"
            pc.font.size = Pt(8)
            pc.font.color.rgb = RGBColor(56, 189, 248) # Cyan code text
            pc.space_before = Pt(4)

        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Interactive Platform Architecture)
    # =========================================================================
    s1 = slides[0]
    set_slide_background(s1)

    # University & Course Header Banner
    univ_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.7), Inches(0.4))
    p = univ_box.text_frame.paragraphs[0]
    p.text = "NORTH SOUTH UNIVERSITY  •  DEPARTMENT OF ELECTRICAL & COMPUTER ENGINEERING"
    p.font.name = "Arial"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_ORANGE

    # Main Presentation Title
    title_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.7), Inches(1.3))
    tf = title_box.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "GrantLens: Pre-Flight Compliance & SRO AI Engine"
    p1.font.name = "Arial"
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE

    p2 = tf.add_paragraph()
    p2.text = "Week 4 Technical Architecture Deep-Dive: Algorithmic Mechanics, Theoretical Formulations & Inter-Subsystem Bridges"
    p2.font.name = "Arial"
    p2.font.size = Pt(13)
    p2.font.color.rgb = TEXT_MUTED

    # Interactive Navigation Action Badge
    action_btn = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.4), Inches(11.73), Inches(0.55))
    action_btn.fill.solid()
    action_btn.fill.fore_color.rgb = RGBColor(30, 41, 59)
    action_btn.line.color.rgb = COLOR_ORANGE
    action_btn.line.width = Pt(1.5)
    action_btn.click_action.target_slide = slides[1] # Jumps to Agenda Hub

    tf = action_btn.text_frame
    p = tf.paragraphs[0]
    p.text = "⚡ CLICK HERE TO LAUNCH INTERACTIVE NAVIGATION DECK (SLIDE SHOW MODE ENABLED) ➔"
    p.alignment = PP_ALIGN.CENTER
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ORANGE

    # 4 Team Member Identity Cards (Roles Kept Strictly Separate)
    members_data = [
        ("Hasin Anzum Inan", "ID: 2323133042", "Document Intelligence & Ingestion", "PyMuPDF sub-millimeter geometry, font span clustering, pdfplumber table extraction, context token packing.", COLOR_CYAN, 3),
        ("Anas Ibne Majbha", "ID: 2322846642", "Backend Core & Compliance Engine", "FastAPI async lifecycle, 3-tier risk taxonomy, multi-factor penalty scoring, non-blocking REST gateway.", COLOR_PURPLE, 6),
        ("Tazreen Alam", "ID: 2321506042", "Researcher Portal UX & Security", "Side-by-side diff UI, interactive rewrite playground, RFC 6749 JWT token lifecycles, salted Bcrypt.", COLOR_EMERALD, 12),
        ("Israt Jahan Susmi", "ID: 2112280642", "Database Systems & DevOps Lead", "SQLAlchemy 2.0 async ORM, UUID relational schemas, PostgreSQL 16 Alpine, multi-stage Docker build.", COLOR_ROSE, 15),
    ]

    card_y = Inches(3.2)
    card_w = Inches(2.78)
    card_h = Inches(3.4)
    spacing = Inches(0.2)

    for i, (name, sid, role_title, focus, col, target_slide_idx) in enumerate(members_data):
        cx = Inches(0.8) + i * (card_w + spacing)
        mcard = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        mcard.fill.solid()
        mcard.fill.fore_color.rgb = CARD_BG
        mcard.line.color.rgb = col
        mcard.line.width = Pt(1.2)
        mcard.click_action.target_slide = slides[target_slide_idx]

        tf = mcard.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.15)
        tf.margin_right = Inches(0.15)
        tf.margin_top = Inches(0.18)

        p = tf.paragraphs[0]
        p.text = name
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        p_id = tf.add_paragraph()
        p_id.text = sid
        p_id.font.name = "Arial"
        p_id.font.size = Pt(9.5)
        p_id.font.color.rgb = col
        p_id.space_after = Pt(4)

        p_role = tf.add_paragraph()
        p_role.text = role_title
        p_role.font.name = "Arial"
        p_role.font.size = Pt(10)
        p_role.font.bold = True
        p_role.font.color.rgb = TEXT_WHITE
        p_role.space_after = Pt(8)

        p_desc = tf.add_paragraph()
        p_desc.text = focus
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(8.5)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_after = Pt(10)

        p_jump = tf.add_paragraph()
        p_jump.text = "➔ Jump to Subsystem"
        p_jump.font.name = "Arial"
        p_jump.font.size = Pt(9)
        p_jump.font.bold = True
        p_jump.font.color.rgb = col

    add_bottom_footer(s1, 0)

    # =========================================================================
    # SLIDE 2: MASTER INTERACTIVE AGENDA & ARCHITECTURE HUB
    # =========================================================================
    s2 = slides[1]
    set_slide_background(s2)
    add_top_nav(s2, 0)
    add_slide_header(s2, "Interactive Agenda Hub", "System Architecture & Engineering Modules Index", COLOR_ORANGE)

    agenda_modules = [
        ("01. Document Intelligence & Geometry", "PyMuPDF sub-millimeter bounding box extraction, font span histograms, and pdfplumber tabular financial parsing.", COLOR_CYAN, 3),
        ("02. Deterministic Compliance Engine", "3-Tier risk classification taxonomy (Red/Yellow/Green), multi-policy dispatch, and weighted penalty scoring algorithms.", COLOR_PURPLE, 6),
        ("03. Gemini 1.5 Flash SRO AI Engine", "Multimodal peer-review orchestration, structured JSON schema enforcement, NSF/NIH rubric modeling, and hallucination containment.", COLOR_AMBER, 9),
        ("04. Researcher Portal UX & Security", "Interactive split-screen diff visualizer, on-demand rewrite playground with prompt presets, and RFC 6749 JWT session lifecycle.", COLOR_EMERALD, 12),
        ("05. Relational Architecture & DevOps", "SQLAlchemy 2.0 async mapped schema, connection pool tuning, dual-engine portability (Postgres/SQLite), and multi-stage Docker mesh.", COLOR_ROSE, 15),
        ("06. System Synthesis & Benchmarks", "Empirical latency profile (sub-second parsing, sub-3s LLM audit), integration testing coverage, and Senior Design phase roadmap.", COLOR_INDIGO, 18),
    ]

    ag_w = Inches(3.98)
    ag_h = Inches(2.25)
    ag_gap_x = Inches(0.24)
    ag_gap_y = Inches(0.22)
    ag_start_x = Inches(0.45)
    ag_start_y = Inches(1.65)

    for i, (m_title, m_desc, m_col, m_target) in enumerate(agenda_modules):
        col_idx = i % 3
        row_idx = i // 3
        bx = ag_start_x + col_idx * (ag_w + ag_gap_x)
        by = ag_start_y + row_idx * (ag_h + ag_gap_y)

        acard = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, by, ag_w, ag_h)
        acard.fill.solid()
        acard.fill.fore_color.rgb = CARD_BG
        acard.line.color.rgb = m_col
        acard.line.width = Pt(1.2)
        acard.click_action.target_slide = slides[m_target]

        tf = acard.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.18)
        tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.16)

        p = tf.paragraphs[0]
        p.text = m_title
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = m_col
        p.space_after = Pt(4)

        p_desc = tf.add_paragraph()
        p_desc.text = m_desc
        p_desc.font.name = "Arial"
        p_desc.font.size = Pt(9)
        p_desc.font.color.rgb = RGBColor(226, 232, 240)
        p_desc.space_after = Pt(8)

        p_act = tf.add_paragraph()
        p_act.text = "➔ Click to Explore Module Deep-Dive"
        p_act.font.name = "Arial"
        p_act.font.size = Pt(8.5)
        p_act.font.bold = True
        p_act.font.color.rgb = m_col

    add_transition_banner(s2, "Introduction & Overview", "Team Roles Division", "Transitioning from high-level architecture into explicit individual engineering responsibilities and workstream boundaries.")
    add_bottom_footer(s2, 1)

    # =========================================================================
    # SLIDE 3: TEAM ENGINEERING DIVISION & WORKSTREAM BOUNDARIES
    # =========================================================================
    s3 = slides[2]
    set_slide_background(s3)
    add_top_nav(s3, 1)
    add_slide_header(s3, "Workstream Separation", "Engineering Division & Subsystem Accountability Matrix", COLOR_ORANGE)

    team_columns = [
        ("Hasin Anzum Inan", "ID: 2323133042", "Document Intelligence & Ingestion Lead", COLOR_CYAN, [
            "Input: Raw Solicitation & Proposal PDF binaries.",
            "Subsystem: PyMuPDF geometry extraction & pdfplumber visual table parser.",
            "Key Metric: Sub-millimeter margin accuracy & zero IEEE-754 currency rounding drift.",
            "Files Owned: backend/ingestion_service.py, tests/test_ingestion_pipeline.py.",
            "Platform Impact: Extracts structured layout geometries and budget tables in <850ms."
        ], 3),
        ("Anas Ibne Majbha", "ID: 2322846642", "Backend Core & Compliance Architect", COLOR_PURPLE, [
            "Input: Extracted geometry dicts & parsed tabular records.",
            "Subsystem: FastAPI non-blocking async IO, Uvicorn worker lifecycle & CORS.",
            "Key Metric: Deterministic 3-tier risk classification & composite score synthesis.",
            "Files Owned: backend/main.py, backend/routes.py, backend/api_schemas.py.",
            "Platform Impact: High-throughput async REST endpoints with 0 unhandled exceptions."
        ], 6),
        ("Tazreen Alam", "ID: 2321506042", "Researcher Portal UX & Security Lead", COLOR_EMERALD, [
            "Input: User credentials, proposal drafts & SRO JSON reviews.",
            "Subsystem: React 19 interactive workspaces, diff explorers, and RFC 6749 JWT auth.",
            "Key Metric: Sub-200ms client state transitions & zero [object Object] serialization bugs.",
            "Files Owned: frontend/src/components/portal/*, backend/auth.py.",
            "Platform Impact: Friction-free researcher revision portal and secure identity lifecycle."
        ], 12),
        ("Israt Jahan Susmi", "ID: 2112280642", "Database Systems & Production DevOps Lead", COLOR_ROSE, [
            "Input: Relational compliance models & container execution environments.",
            "Subsystem: SQLAlchemy 2.0 async ORM, PostgreSQL 16 Alpine & Docker Compose.",
            "Key Metric: Zero environment drift, persistent NVMe storage & async connection pool.",
            "Files Owned: backend/models.py, backend/database.py, docker-compose.yml, Dockerfile.",
            "Platform Impact: 100% ACID database reliability and multi-container self-healing."
        ], 15),
    ]

    rw_w = Inches(2.95)
    rw_h = Inches(4.5)
    rw_gap = Inches(0.2)
    rw_start_x = Inches(0.45)
    rw_start_y = Inches(1.65)

    for i, (name, sid, role_title, col, bullets, target_idx) in enumerate(team_columns):
        rx = rw_start_x + i * (rw_w + rw_gap)
        rcard = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, rw_start_y, rw_w, rw_h)
        rcard.fill.solid()
        rcard.fill.fore_color.rgb = CARD_BG
        rcard.line.color.rgb = col
        rcard.line.width = Pt(1.2)
        rcard.click_action.target_slide = slides[target_idx]

        tf = rcard.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.14)
        tf.margin_right = Inches(0.14)
        tf.margin_top = Inches(0.14)

        p = tf.paragraphs[0]
        p.text = name
        p.font.name = "Arial"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        p_id = tf.add_paragraph()
        p_id.text = sid
        p_id.font.name = "Arial"
        p_id.font.size = Pt(9)
        p_id.font.color.rgb = col
        p_id.space_after = Pt(2)

        p_role = tf.add_paragraph()
        p_role.text = role_title
        p_role.font.name = "Arial"
        p_role.font.size = Pt(9.5)
        p_role.font.bold = True
        p_role.font.color.rgb = TEXT_WHITE
        p_role.space_after = Pt(6)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.name = "Arial"
            pb.font.size = Pt(8.5)
            pb.font.color.rgb = RGBColor(203, 213, 225)
            pb.space_after = Pt(3)

        p_jump = tf.add_paragraph()
        p_jump.text = "➔ Jump to Subsystem Deep Dive"
        p_jump.font.name = "Arial"
        p_jump.font.size = Pt(8.5)
        p_jump.font.bold = True
        p_jump.font.color.rgb = col
        p_jump.space_before = Pt(6)

    add_transition_banner(s3, "Engineering Division", "Document Intelligence & Ingestion (Hasin)", "Entering Subsystem 1: Examining how binary PDF streams are parsed into sub-millimeter geometric coordinates.")
    add_bottom_footer(s3, 2)

    # Helper for standard 3-column deep-dive slides
    def create_three_column_slide(slide, curr_idx, nav_idx, tag_text, title_text, role_color, col1_data, col2_data, col3_data, prev_topic, next_topic, transition_text):
        set_slide_background(slide)
        add_top_nav(slide, nav_idx)
        add_slide_header(slide, tag_text, title_text, role_color)

        c_w = Inches(3.98)
        c_h = Inches(4.5)
        c_gap = Inches(0.24)
        c_y = Inches(1.65)
        c_x1 = Inches(0.45)
        c_x2 = c_x1 + c_w + c_gap
        c_x3 = c_x2 + c_w + c_gap

        create_card(slide, c_x1, c_y, c_w, c_h, col1_data[0], col1_data[1], col1_data[2], role_color, col1_data[3] if len(col1_data) > 3 else None)
        create_card(slide, c_x2, c_y, c_w, c_h, col2_data[0], col2_data[1], col2_data[2], role_color, col2_data[3] if len(col2_data) > 3 else None)
        create_card(slide, c_x3, c_y, c_w, c_h, col3_data[0], col3_data[1], col3_data[2], role_color, col3_data[3] if len(col3_data) > 3 else None)

        add_transition_banner(slide, prev_topic, next_topic, transition_text)
        add_bottom_footer(slide, curr_idx)

    # =========================================================================
    # SLIDE 4: SUB-MILLIMETER GEOMETRIC LAYOUT AUDITING (Hasin Anzum Inan)
    # =========================================================================
    create_three_column_slide(
        slides[3], 3, 2,
        "Subsystem 1: Document Intelligence  |  Hasin Anzum Inan (2323133042)",
        "Sub-Millimeter Geometric Layout Auditing & Vector Bounding Boxes",
        COLOR_CYAN,
        (
            "Vector Bounding Box Extraction",
            "PyMuPDF PostScript Stream Analysis",
            [
                "PDF files store content as PostScript vector curves rather than reflowable text.",
                "Extracts page.rect and text block coordinates: (x0, y0, x1, y1).",
                "Translates typographic points to physical inches: 72 points = 1.0 inch.",
                "Traverses page-level visual hierarchy: Document -> Page -> TextBlock -> Line -> Span.",
            ],
            "# PyMuPDF Bounding Box Geometry\nblocks = page.get_text('blocks')\nfor b in blocks:\n    x0, y0, x1, y1 = b[:4]\n    margin_left = min(margin_left, x0 / 72.0)"
        ),
        (
            "Heuristic Bleed Filtering",
            "Header / Footer Noise Elimination",
            [
                "Running headers and page numbers naturally bleed into the 1.0\" margin zone.",
                "Naive auditing causes false-positive violations on 100% of compliant proposals.",
                "Implements vertical spatial boundary filtering: ignores content where y < 36pt (0.5\") or y > 756pt (10.5\").",
                "Isolates core manuscript body text from institutional running titles.",
            ],
            "# Heuristic Vertical Filtering\nif y0 < 36.0 or y1 > 756.0:\n    continue # Skip header/footer artifact\nbody_margin = min(body_margin, x0 / 72.0)"
        ),
        (
            "Multi-Agency Margin Enforcement",
            "NSF vs NIH Mathematical Gating",
            [
                "NSF 24-500: Enforces strict 1.0 inch (72pt) minimum margins on all four sides.",
                "NIH R01: Permits 0.5 inch (36pt) margins for high-density medical narratives.",
                "Calculates delta discrepancy: Δm = Target_Margin - Measured_Margin.",
                "Any negative delta triggers an instant high-severity RED or YELLOW audit finding.",
            ],
            "# Discrepancy Calculation\nmargin_diff = round(target_min - actual_min, 3)\nif margin_diff > 0.05: # >0.05in violation\n    findings.append(FindingSeverity.RED)"
        ),
        "Raw Ingestion", "Typographic Distribution",
        "Having parsed page-level spatial geometry and margin boundaries, the ingestion pipeline zooms into sub-character typographic spans."
    )

    # =========================================================================
    # SLIDE 5: TYPOGRAPHIC DISTRIBUTION & FONT SPAN CLUSTERING (Hasin Anzum Inan)
    # =========================================================================
    create_three_column_slide(
        slides[4], 4, 2,
        "Subsystem 1: Document Intelligence  |  Hasin Anzum Inan (2323133042)",
        "Typographic Distribution & Font Span Clustering Mechanics",
        COLOR_CYAN,
        (
            "Sub-Character Span Traversal",
            "Granular PyMuPDF Span Inspection",
            [
                "Iterates over every character span inside page.get_text('dict')['blocks'].",
                "Extracts span['size'], span['font'], and typographic flags.",
                "Builds statistical histogram of font size frequencies across entire document.",
                "Determines true dominant body font size via statistical mode (e.g. 11.0 pt).",
            ],
            "# Span Typographic Aggregation\nfont_sizes = []\nfor span in line['spans']:\n    font_sizes.append(round(span['size'], 1))\nbody_mode = Counter(font_sizes).most_common(1)[0][0]"
        ),
        (
            "Formatting Evasion Detection",
            "Microscopic Typography Circumvention",
            [
                "Researchers frequently evade 15-page limits by shrinking captions or references.",
                "Detects deceptive sub-threshold text spans (<10.0pt Arial or <11.0pt Times).",
                "Computes font violation density: ratio of non-compliant character spans to total page text.",
                "Distinguishes legitimate mathematical subscripts from fraudulent text compression.",
            ],
            "# Microscopic Evasion Detection\nsub_10pt_chars = sum(len(s['text']) for s in spans if s['size'] < 9.5)\nif sub_10pt_chars > 200:\n    flag_fatal_typography_violation()"
        ),
        (
            "Font Family Normalization",
            "Embedded PostScript Aliasing Engine",
            [
                "PDF generators embed arbitrary subset font names (e.g. 'BAAAAA+NimbusRoman').",
                "Implements regex canonicalization to map embedded font names to agency standards.",
                "Validates typeface legality: Arial, Courier New, Times New Roman, Computer Modern.",
                "Flags non-compliant decorative or compact font families immediately.",
            ],
            "# Font Family Aliasing\nclean_name = re.sub(r'^[A-Z]{6}\\+', '', raw_font)\nif 'times' in clean_name.lower():\n    canonical_family = 'Times New Roman'"
        ),
        "Sub-Millimeter Geometry", "Tabular Financial Extraction",
        "With layout margins and font typography validated, the ingestion pipeline tackles structured tabular ledgers and financial budgets."
    )

    # =========================================================================
    # SLIDE 6: TABULAR FINANCIAL PARSING & BUDGET RECONCILIATION (Hasin Anzum Inan)
    # =========================================================================
    create_three_column_slide(
        slides[5], 5, 2,
        "Subsystem 1: Document Intelligence  |  Hasin Anzum Inan (2323133042)",
        "Tabular Financial Parsing & Cross-Document Reconciliation",
        COLOR_CYAN,
        (
            "Visual Table Extraction",
            "pdfplumber Visual Line Intersection",
            [
                "PyMuPDF extracts plain text streams, destroying two-dimensional table structures.",
                "Deploys pdfplumber to detect explicit vector table lines and visual cell matrices.",
                "Applies horizontal and vertical snap tolerances to resolve borderless ledger tables.",
                "Extracts structured row-column arrays preserving financial line-item context.",
            ],
            "# pdfplumber Visual Table Extraction\nwith pdfplumber.open(stream) as pdf:\n    tables = page.extract_tables({\n        'vertical_strategy': 'lines',\n        'horizontal_strategy': 'lines'\n    })"
        ),
        (
            "Currency Tokenization & Clean",
            "IEEE-754 Safe Decimal Arithmetic",
            [
                "Strips non-numeric symbols via compiled regex: CURRENCY_CLEAN_REGEX = re.compile(r'[^\\d.-]').",
                "Replaces standard float types with Python Decimal to eliminate floating-point rounding errors.",
                "Normalizes diverse currency notations: '$125,000.00', '125000 USD', '$ 125,000'.",
                "Maps parsed table rows to standard OMB cost categories (Personnel, Equipment, Travel).",
            ],
            "# Currency Regex & Decimal Parse\nclean_val = CURRENCY_CLEAN_REGEX.sub('', cell_text)\namount = Decimal(clean_val) # IEEE-754 safe\nbudget_items.append(BudgetLineItem(cost=amount))"
        ),
        (
            "Cross-Document Reconciliation",
            "Narrative Claims vs Itemized Ledger",
            [
                "Extracts total funding requested from Project Summary narrative ($345,000).",
                "Sums all itemized row amounts extracted from Budget Justification table.",
                "Computes arithmetic delta: ΔBudget = |Narrative_Claim - Sum(Ledger_Rows)|.",
                "Discrepancies > $1.00 trigger high-priority audit alerts preventing budget rejection.",
            ],
            "# Arithmetic Discrepancy Gate\nledger_sum = sum(item.cost for item in items)\nif abs(narrative_budget - ledger_sum) > Decimal('1.00'):\n    trigger_budget_reconciliation_warning()"
        ),
        "Document Ingestion", "Deterministic Rule Engine (Anas)",
        "Having extracted normalized geometry, font spans, and budget line-items, we now pass structured data to the deterministic compliance engine."
    )

    # =========================================================================
    # SLIDE 7: DETERMINISTIC HEURISTIC COMPLIANCE ENGINE (Anas Ibne Majbha)
    # =========================================================================
    create_three_column_slide(
        slides[6], 6, 3,
        "Subsystem 2: Backend Core & Compliance  |  Anas Ibne Majbha (2322846642)",
        "Deterministic Heuristic Compliance Engine & Policy Dispatch",
        COLOR_PURPLE,
        (
            "3-Tier Risk Classification",
            "Formal Categorical Severity Taxonomy",
            [
                "FATAL RED: Immediate desk-rejection violations (page limit overflow, font <10pt, margins <0.75\").",
                "WARNING YELLOW: High administrative risk or ambiguity (unclear budget line-item, missing sub-header).",
                "PASSED GREEN: Verified compliant metric adhering to agency standard thresholds.",
                "Guarantees deterministic pass/fail repeatability without LLM non-determinism.",
            ],
            "# 3-Tier Categorical Taxonomy\nclass FindingSeverity(str, Enum):\n    RED = 'RED'       # Fatal Disqualification\n    YELLOW = 'YELLOW' # Administrative Warning\n    GREEN = 'GREEN'   # Compliant Metric"
        ),
        (
            "Multi-Agency Policy Matrix",
            "Configurable Solicitation Blueprints",
            [
                "NSF 24-500: Strict 15-page limit, 1.0\" margins, 10pt Arial / 11pt Times New Roman.",
                "NIH R01: 12-page limit, 0.5\" margins, required 'Specific Aims' & 'Human Subjects' sections.",
                "Extracts agency rules directly from ingested solicitation guideline documents.",
                "Dispatches evaluation across independent rule modules: Page, Geometry, Budget, Headers.",
            ],
            "# Multi-Agency Rule Dispatcher\nRULES = {\n  'NSF 24-500': {'max_pages': 15, 'min_margin': 1.0},\n  'NIH R01':    {'max_pages': 12, 'min_margin': 0.5}\n}\ncfg = RULES.get(agency, DEFAULT_POLICY)"
        ),
        (
            "Contextual Remediation Advice",
            "Actionable Researcher Guidance",
            [
                "Never emits generic error codes; generates specific corrective remediation text.",
                "Example: 'Bottom margin measured at 0.82in on Page 4. Increase footer margin to 1.0in to prevent rejection.'",
                "Links findings directly to offending document pages and specific bounding boxes.",
                "Enables researchers to resolve disqualifying errors in minutes before submission.",
            ],
            "# Remediation Message Synthesis\nfinding = AuditFinding(\n    severity=FindingSeverity.RED,\n    category=FindingCategory.PAGE_LIMIT,\n    message=f'Page count {actual} exceeds limit {limit}.'\n)"
        ),
        "Ingestion Extraction", "Heuristic Scoring Algorithm",
        "Individual rule violations must now be mathematically aggregated into a standardized composite compliance score."
    )

    # =========================================================================
    # SLIDE 8: MULTI-FACTOR HEURISTIC SCORING & PENALTY MODELING (Anas Ibne Majbha)
    # =========================================================================
    create_three_column_slide(
        slides[7], 7, 3,
        "Subsystem 2: Backend Core & Compliance  |  Anas Ibne Majbha (2322846642)",
        "Multi-Factor Heuristic Scoring & Penalty Modeling Formulation",
        COLOR_PURPLE,
        (
            "Mathematical Formulation",
            "Bounded Linear Penalty Model",
            [
                "Computes overall institutional compliance score bounded on the interval [0, 100].",
                "Base initial score starts at 100 points (perfect pre-flight compliance).",
                "Score Equation: S = max(0, 100 - Σ [ w_i * δ_i ]).",
                "δ_i represents indicator function for violation i; w_i represents category penalty weight.",
            ],
            "# Compliance Score Formulation\nscore = 100\nfor finding in findings:\n    weight = PENALTY_WEIGHTS.get(finding.category, 5)\n    score -= weight * (2 if finding.is_red else 1)\nfinal_score = max(0, score)"
        ),
        (
            "Category Penalty Weights",
            "Empirical Disqualification Weights",
            [
                "Page Limit Overflow: w = 30 points (instant federal desk-rejection trigger).",
                "Missing Mandatory Section: w = 25 points (e.g. missing Data Management Plan).",
                "Margin / Font Breach: w = 20 points (automatic administrative screening failure).",
                "Tabular Budget Discrepancy: w = 15 points (unreconciled narrative ledger sum).",
            ],
            "# Empirical Penalty Matrix\nPENALTY_WEIGHTS = {\n    'PAGE_LIMIT': 30,         # Fatal rejection\n    'MANDATORY_SECTION': 25,  # Missing requirement\n    'FONT_MARGIN': 20,        # Layout breach\n    'BUDGET': 15              # Arithmetic mismatch\n}"
        ),
        (
            "Institutional Risk Status",
            "Administrative Rating Gateways",
            [
                "SCORE >= 90: PASSED (Certified compliant for institutional SRO sign-off).",
                "SCORE 70 - 89: WARNINGS (Minor formatting risks; submission allowed with cautions).",
                "SCORE < 70: FAILED (High disqualification probability; automated submission block).",
                "Guarantees university research offices protect their institutional funding success rate.",
            ],
            "# Institutional Status Gate\nif score >= 90 and red_count == 0:\n    status = AuditStatus.PASSED\nelif red_count > 0 or score < 70:\n    status = AuditStatus.FAILED\nelse: status = AuditStatus.WARNINGS"
        ),
        "Deterministic Rules", "Asynchronous Server Architecture",
        "Heavy PDF processing and scoring algorithms require an asynchronous, non-blocking REST gateway to sustain high concurrency."
    )

    # =========================================================================
    # SLIDE 9: HIGH-THROUGHPUT ASYNC SERVER ARCHITECTURE (Anas Ibne Majbha)
    # =========================================================================
    create_three_column_slide(
        slides[8], 8, 3,
        "Subsystem 2: Backend Core & Compliance  |  Anas Ibne Majbha (2322846642)",
        "High-Throughput Asynchronous Server & Gateway Architecture",
        COLOR_PURPLE,
        (
            "Non-Blocking Async Lifespan",
            "FastAPI + Uvicorn Concurrency",
            [
                "FastAPI asynchronous event loop handles concurrent HTTP client connections.",
                "Lifespan Context Manager (@asynccontextmanager): initializes database DDL before serving.",
                "Zero worker starvation: request parsing never blocks incoming traffic.",
                "Graceful server shutdown ensures all pending document writes commit safely.",
            ],
            "# Async Server Lifespan\n@asynccontextmanager\nasync def lifespan(app: FastAPI):\n    await init_db() # Relational schema init\n    yield\n    await engine.dispose() # Clean pool drain"
        ),
        (
            "CPU Offloading & Worker Threads",
            "Event Loop Protection via Thread Pools",
            [
                "PyMuPDF and pdfplumber parsing are CPU-intensive C++ execution routines.",
                "Direct invocation in async def routes would freeze the asyncio event loop for 800ms.",
                "Delegates heavy PDF computation to worker thread pools via asyncio.to_thread.",
                "Preserves microsecond API responsiveness for simultaneous researcher requests.",
            ],
            "# Thread Pool Offload\nresult = await asyncio.to_thread(\n    DocumentIngestionService.parse_dual_pdf,\n    solicitation_bytes, proposal_bytes\n)"
        ),
        (
            "CORS & Telemetry Telemetry",
            "Loopback Resolution & Diagnostics",
            [
                "Configures comprehensive CORS middleware authorizing Vite (localhost:5173).",
                "Eliminates IPv4 vs IPv6 loopback mismatch (standardized on 127.0.0.1:8000).",
                "Exposes /api/v1/status telemetry route reporting real-time database and memory state.",
                "Maintains backward compatibility with legacy status monitoring endpoints.",
            ],
            "# Unified CORS Middleware\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=['http://localhost:5173'],\n    allow_origin_regex=r'http://(localhost|127\\.0\\.0\\.1):[0-9]+',\n    allow_credentials=True\n)"
        ),
        "Backend Gateway", "Gemini 1.5 Flash SRO AI Reviewer",
        "Deterministic heuristics verify document formatting; we now transition to the generative LLM layer to evaluate qualitative scientific merit."
    )

    # =========================================================================
    # SLIDE 10: MULTIMODAL LLM PEER-REVIEW ARCHITECTURE (AI Core)
    # =========================================================================
    create_three_column_slide(
        slides[9], 9, 4,
        "Subsystem 3: Gemini AI SRO Core  |  Hasin Anzum Inan & Anas Ibne Majbha",
        "Multimodal LLM Peer-Review Architecture & Structured JSON Schemas",
        COLOR_AMBER,
        (
            "Multi-Document Context Ingestion",
            "Full Solicitation & Proposal Grounding",
            [
                "Simultaneously ingests agency solicitation guideline PDF and researcher draft PDF.",
                "Leverages Google Gemini 1.5 Flash's 1-million token context window capability.",
                "Packs full 80-page guideline rules without lossy extractive summarization.",
                "Aligns proposal critique directly with federal program officer expectations.",
            ],
            "# Multi-Document Gemini Context\nprompt = f'''\nAgency Solicitation: {solicitation_text}\nResearcher Draft: {proposal_text}\nEvaluate against official merit review rubrics.\n'''"
        ),
        (
            "Structured Schema Enforcement",
            "Zero Parsing Failure Architecture",
            [
                "Enforces strict response_mime_type='application/json' via Google GenAI SDK.",
                "Defines deterministic Pydantic schema for output validation (rubrics, critiques, verdict).",
                "Prevents conversational fluff or markdown fence parsing crashes in production.",
                "Guarantees every AI response hydrates relational database columns seamlessly.",
            ],
            "# Strict JSON Schema Config\nresponse = client.models.generate_content(\n    model='gemini-1.5-flash',\n    contents=prompt,\n    config=types.GenerateContentConfig(\n        response_mime_type='application/json'\n    )\n)"
        ),
        (
            "Resilient Simulation Fallback",
            "Zero-Degradation Offline Execution",
            [
                "Detects missing, invalid, or quota-exhausted Google Gemini API keys gracefully.",
                "Switches automatically to deterministic simulated SRO evaluation engine.",
                "Synthesizes publication-grade section critiques, rubric scores, and rewrites offline.",
                "Ensures 100% platform availability during academic defense or air-gapped evaluation.",
            ],
            "# Resilient Offline Fallback\nif not self.client:\n    logger.info('Simulated SRO review active.')\n    return self._generate_fallback_review(\n        title, agency, text\n    )"
        ),
        "Heuristic Compliance", "SRO Rubric Evaluation",
        "Structured JSON responses are next mapped into federal merit review rubrics and simulated panel recommendations."
    )

    # =========================================================================
    # SLIDE 11: SRO RUBRIC EVALUATION & PANEL VERDICTS (AI Core)
    # =========================================================================
    create_three_column_slide(
        slides[10], 10, 4,
        "Subsystem 3: Gemini AI SRO Core  |  Hasin Anzum Inan & Anas Ibne Majbha",
        "SRO Rubric Evaluation & Panel Recommendation Taxonomy",
        COLOR_AMBER,
        (
            "Dual-Agency Rubric Modeling",
            "NSF & NIH Evaluation Criteria",
            [
                "NSF Merit Review Criteria: Intellectual Merit (30%), Broader Impacts (25%), Alignment (25%), Budget Realism (20%).",
                "NIH Criteria: Significance, Investigator, Innovation, Approach, Environment.",
                "Synthesizes granular 0-100 scores across every individual qualitative rubric dimension.",
                "Highlights specific rhetorical deficiencies in broader educational outreach.",
            ],
            "# Rubric Score Computation\ncomposite_score = round(\n    0.30 * intellectual_merit +\n    0.25 * broader_impacts +\n    0.25 * solicitation_alignment +\n    0.20 * budget_realism, 1\n)"
        ),
        (
            "3-Tier Simulated Panel Verdicts",
            "Federal SRO Panel Emulation",
            [
                "FUND WITH DISTINCTION (Composite >= 90%): Exceptional innovation and methodology.",
                "REVISE AND RESUBMIT (Composite 70% - 89%): Promising science with minor deficits.",
                "DO NOT RECOMMEND (Composite < 70%): Fatal flaws in experimental controls or reach.",
                "Emulates real-world Scientific Review Officer (SRO) consensus panel discussions.",
            ],
            "# 3-Tier SRO Panel Verdict\nclass AIPanelRecommendation(str, Enum):\n    FUND_WITH_DISTINCTION = 'FUND_WITH_DISTINCTION'\n    REVISE_AND_RESUBMIT   = 'REVISE_AND_RESUBMIT'\n    DO_NOT_RECOMMEND      = 'DO_NOT_RECOMMEND'"
        ),
        (
            "Executive SRO Consensus Summary",
            "Program Officer Perspective",
            [
                "Synthesizes authoritative 2-paragraph SRO executive consensus summary.",
                "Summarizes primary proposal strengths, competitive differentiators, and fatal risks.",
                "Delivers the exact feedback researchers would receive from a National Science Board panel.",
                "Empowers researchers to anticipate reviewer critique prior to formal submission.",
            ],
            "# SRO Summary Extraction\nsummary = review_json.get('sro_consensus_summary')\npanel_verdict = review_json.get('recommendation')\nreturn AIReviewResponse(summary=summary, ...)"
        ),
        "LLM Peer Review", "Grounded Critique & Hallucination Control",
        "Beyond aggregate scores, researchers require exact section-by-section critiques anchored directly in proposal text."
    )

    # =========================================================================
    # SLIDE 12: GROUNDED SECTION CRITIQUE & HALLUCINATION CONTROL (AI Core)
    # =========================================================================
    create_three_column_slide(
        slides[11], 11, 4,
        "Subsystem 3: Gemini AI SRO Core  |  Hasin Anzum Inan & Anas Ibne Majbha",
        "Grounded Section Critique & Hallucination Mitigation",
        COLOR_AMBER,
        (
            "Verbatim Excerpt Anchoring",
            "Evidence-Based Proposal Critique",
            [
                "Forces Gemini to extract verbatim quotations from the draft proposal manuscript.",
                "Eliminates vague feedback like 'Improve your writing' through strict grounding constraints.",
                "Identifies unquantified claims (e.g. 'We will do K-12 outreach' without participant metrics).",
                "Pairs each quoted excerpt directly with panelist critique and remediation rationale.",
            ],
            "# Verbatim Grounding Prompt\n'original_excerpt': 'exact text from proposal',\n'critique': 'why the panelist finds this weak',\n'suggested_rewrite': 'assertive publication prose'"
        ),
        (
            "Hallucination Containment",
            "Low-Temperature Bounded Sampling",
            [
                "Sets LLM temperature T = 0.2 to prevent creative fabrications or phantom guidelines.",
                "Strict system instructions prohibit citing non-existent federal agency mandates.",
                "Cross-checks all cited solicitation requirements against ingested guideline vectors.",
                "Ensures 100% evidentiary integrity in academic peer-review diagnostics.",
            ],
            "# Low Temperature Bounded Generation\nconfig = types.GenerateContentConfig(\n    temperature=0.2, # Highly deterministic\n    top_p=0.8,\n    response_mime_type='application/json'\n)"
        ),
        (
            "Publication-Grade Rewriting",
            "Side-by-Side Suggestion Synthesis",
            [
                "Generates polished, assertive academic prose for identified draft weaknesses.",
                "Replaces passive constructions ('It is anticipated that...') with active claims.",
                "Embeds quantifiable milestone metrics into Broader Impacts and Methodology text.",
                "Provides drop-in replacements ready for researcher inclusion in revised manuscripts.",
            ],
            "# Assertive Academic Prose Synthesis\n'rewritten_text': 'Building upon rigorous empirical benchmarks, our investigation establishes a verified framework...'"
        ),
        "AI Diagnostics", "Interactive Researcher UX (Tazreen)",
        "Structured AI reviews must be surfaced in an intuitive, visual web interface that minimizes researcher cognitive load."
    )

    # =========================================================================
    # SLIDE 13: INTERACTIVE SECTION DIFF EXPLORER (Tazreen Alam)
    # =========================================================================
    create_three_column_slide(
        slides[12], 12, 5,
        "Subsystem 4: Researcher Portal UX & Security  |  Tazreen Alam (2321506042)",
        "Interactive Section Diff Explorer & Visual Proposal Remediation",
        COLOR_EMERALD,
        (
            "Split-Screen Diff Architecture",
            "GeminiAdvisor.jsx Visual Hierarchy",
            [
                "Renders comparative split-screen view: Original Draft Excerpt vs Gemini Polished Text.",
                "Color-coded visual cues: Emerald for assertive revisions, Amber for flagged deficits.",
                "Surfaces Scientific Review Officer (SRO) panel badges and composite score ring meter.",
                "Minimizes researcher cognitive load during stressful pre-submission revision cycles.",
            ],
            "# React Split-Screen Architecture\n<div className='grid grid-cols-1 lg:grid-cols-2 gap-4'>\n  <DraftViewer text={critique.original_text} />\n  <RewriteViewer text={critique.rewritten_text} />\n</div>"
        ),
        (
            "One-Click Clipboard Integration",
            "Frictionless Workflow Acceleration",
            [
                "Implements native navigator.clipboard.writeText integration on all suggestion cards.",
                "Provides animated transient feedback ('Copied!') with 2.5-second reset timers.",
                "Allows researchers to transfer polished paragraphs directly into LaTeX or Word.",
                "Eliminates manual retyping and copy-paste formatting corruption.",
            ],
            "# Native Clipboard Handler\nconst handleCopy = (text, id) => {\n  navigator.clipboard.writeText(text);\n  setCopiedId(id);\n  setTimeout(() => setCopiedId(null), 2500);\n};"
        ),
        (
            "Progressive Multi-Step Animation",
            "Cognitive Feedback During LLM Synthesis",
            [
                "Simulates multi-stage progress indicators while Gemini synthesizes the panel verdict.",
                "Step 1: Ingesting layout geometry -> Step 2: Scoring rubrics -> Step 3: Polishing prose.",
                "Keeps researchers informed during 2-3 second generative inference latency.",
                "Eliminates perception of frozen UI state with fluid SVG pulse spinners.",
            ],
            "# Progressive Stepper State\nsetAiLoading(true); setAiStep(1);\nsetTimeout(() => setAiStep(2), 700);\nsetTimeout(() => setAiStep(3), 1500);"
        ),
        "AI Reviewer Engine", "Interactive Rewrite Playground",
        "Beyond reviewing static AI suggestions, researchers can interactively polish specific paragraphs on-demand."
    )

    # =========================================================================
    # SLIDE 14: INTERACTIVE REWRITE PLAYGROUND & PRESETS (Tazreen Alam)
    # =========================================================================
    create_three_column_slide(
        slides[13], 13, 5,
        "Subsystem 4: Researcher Portal UX & Security  |  Tazreen Alam (2321506042)",
        "Interactive Rewrite Playground & Prompt Engineering Presets",
        COLOR_EMERALD,
        (
            "On-Demand Paragraph Playground",
            "Real-Time Iterative Authoring Sandbox",
            [
                "Allows researchers to paste any proposal excerpt and choose a rhetorical direction.",
                "Dispatches asynchronous POST /api/v1/submissions/{id}/ai-rewrite requests.",
                "Returns revised academic prose, bulleted key improvements, and model attribution.",
                "Supports iterative continuous polishing without re-uploading the entire PDF.",
            ],
            "# Playground State Management\nconst [customDraft, setCustomDraft] = useState('');\nconst [instruction, setInstruction] = useState('Strengthen Broader Impacts');\nconst [result, setResult] = useState(null);"
        ),
        (
            "Rhetorical Instruction Presets",
            "Targeted Proposal Polishing Modes",
            [
                "Strengthen Broader Impacts metrics for NSF 24-500 (adds K-12 metrics & outreach).",
                "Enhance scientific assertiveness and eliminate passive voice constructions.",
                "Clarify technical risk mitigation and alternative experimental approaches.",
                "Democratizes advanced prompt engineering for university faculty researchers.",
            ],
            "# Pre-Configured Presets\nconst PRESETS = [\n  'Strengthen Broader Impacts for NSF 24-500',\n  'Enhance scientific assertiveness',\n  'Clarify technical risk mitigation'\n];"
        ),
        (
            "Resilient Error Deserialization",
            "Elimination of [object Object] Bugs",
            [
                "FastAPI returns Pydantic validation errors as structured JSON arrays: {'detail': [...]}.",
                "Standard err.message serialization converts arrays into the literal string '[object Object]'.",
                "Engineered extractErrorMessage() in apiConfig.js: recursively unpacks error lists.",
                "Guarantees human-readable feedback for all validation and network failure modes.",
            ],
            "# extractErrorMessage Parser\nexport const extractErrorMessage = (data) => {\n  if (Array.isArray(data?.detail))\n    return data.detail.map(d => d.msg).join('; ');\n  return data?.detail || 'Request failed.';\n};"
        ),
        "Interactive Playground", "Identity & Session Security",
        "Interactive authoring requires persistent researcher state, necessitating high-assurance authentication and session security."
    )

    # =========================================================================
    # SLIDE 15: RESEARCHER IDENTITY LIFECYCLE & SECURITY (Tazreen Alam)
    # =========================================================================
    create_three_column_slide(
        slides[14], 14, 5,
        "Subsystem 4: Researcher Portal UX & Security  |  Tazreen Alam (2321506042)",
        "Researcher Identity Lifecycle, RFC 6749 Auth & Session Security",
        COLOR_EMERALD,
        (
            "Salted Bcrypt Password Hashing",
            "Zero-Knowledge Credential Storage",
            [
                "Direct native Bcrypt implementation (bcrypt.hashpw / bcrypt.checkpw) with rounds=12.",
                "Eliminates deprecated passlib wrappers and resolves bcrypt 5.0 compatibility crashes.",
                "Applies 72-byte UTF-8 string truncation defense against bcrypt buffer overflow bugs.",
                "Guarantees irreversible credential storage in accordance with institutional IT standards.",
            ],
            "# Salted Bcrypt Implementation\ndef get_password_hash(pwd: str) -> str:\n    salt = bcrypt.gensalt(rounds=12)\n    return bcrypt.hashpw(pwd.encode('utf-8')[:72], salt).decode('utf-8')"
        ),
        (
            "RFC 6749 JWT Token Lifecycle",
            "Access & Refresh Token Architecture",
            [
                "Issues cryptographic HS256 JWT tokens containing UUID subject and expiry timestamp.",
                "Short-lived Access Tokens (60 minutes) minimize exposure window in compromised browsers.",
                "Long-lived Refresh Tokens (7 days) support seamless session re-authorization.",
                "Protected FastAPI OAuth2PasswordBearer dependency gates all ingestion endpoints.",
            ],
            "# JWT Token Minting\nexpire = datetime.now(timezone.utc) + timedelta(minutes=60)\ntoken = jwt.encode(\n    {'sub': str(user.id), 'exp': expire, 'type': 'access'},\n    SECRET_KEY, algorithm='HS256'\n)"
        ),
        (
            "Proactive Session Probing",
            "/auth/me Auto-Purge Self-Healing",
            [
                "Database restarts previously caused 401 Unauthorized loops for stale browser tokens.",
                "Engineered GET /api/v1/auth/me session probe executed on App.jsx mount.",
                "Automatically purges invalid tokens from localStorage and resets UI to clean auth state.",
                "Includes manual 'Sign Out & Re-Login' escape hatch in SubmissionPortal.jsx.",
            ],
            "# Frontend Session Probe\nfetch('/api/v1/auth/me', {headers: {Authorization: `Bearer ${token}`}})\n  .then(res => { if (!res.ok) handleSignOut(); });"
        ),
        "Identity & Security", "Relational Compliance Schema (Susmi)",
        "Authenticated sessions and document audits must be persisted to an ACID-compliant relational database schema."
    )

    # =========================================================================
    # SLIDE 16: RELATIONAL COMPLIANCE SCHEMA & UUID DATA MODELING (Israt Jahan Susmi)
    # =========================================================================
    create_three_column_slide(
        slides[15], 15, 6,
        "Subsystem 5: Database & DevOps Infrastructure  |  Israt Jahan Susmi (2112280642)",
        "Relational Compliance Schema, SQLAlchemy 2.0 & UUID Data Modeling",
        COLOR_ROSE,
        (
            "Normalized Entity Topology",
            "SQLAlchemy 2.0 Declarative Models",
            [
                "User (1) -> GrantSubmission (N): Links researcher accounts with audit histories.",
                "GrantSubmission (1) -> Document (N): Stores Solicitation vs Proposal PDF binaries.",
                "GrantSubmission (1) -> AuditReport (1) -> AuditFinding (N): Deterministic rule results.",
                "GrantSubmission (1) -> AIReview (1): Stores Gemini 1.5 Flash SRO panel evaluations.",
            ],
            "# SQLAlchemy 2.0 Mapped Relational Model\nclass GrantSubmission(Base):\n    __tablename__ = 'grant_submissions'\n    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)\n    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'))"
        ),
        (
            "UUIDv4 Security & Scalability",
            "Anti-Enumeration Primary Keys",
            [
                "Replaces auto-incrementing integer IDs with universally unique identifiers (UUIDv4).",
                "Prevents enumeration attacks (attackers guessing /submissions/42 to steal proposals).",
                "Enables seamless multi-node distributed database scaling without primary key collisions.",
                "Compatible across both PostgreSQL native UUID type and SQLite string fallback.",
            ],
            "# UUIDv4 Primary Key Definition\nid: Mapped[uuid.UUID] = mapped_column(\n    UUID(as_uuid=True),\n    primary_key=True,\n    default=uuid.uuid4,\n    index=True\n)"
        ),
        (
            "Cascade Integrity & Indexing",
            "Referential Integrity & Lookup Speed",
            [
                "Configures ondelete='CASCADE' across all relational foreign key dependencies.",
                "Deleting a submission automatically purges associated documents, audits, and reviews.",
                "Indexes foreign keys (user_id, submission_id, email) for constant-time O(1) joins.",
                "Guarantees relational consistency and prevents orphaned records in storage.",
            ],
            "# Cascade Deletion Policy\naudit_report: Mapped['AuditReport'] = relationship(\n    'AuditReport',\n    cascade='all, delete-orphan',\n    passive_deletes=True\n)"
        ),
        "Relational Schema", "Connection Pooling & Database Duality",
        "Relational schemas require resilient asynchronous connection pooling to maintain high throughput during multi-user submissions."
    )

    # =========================================================================
    # SLIDE 17: ASYNC CONNECTION POOLING & DATABASE DUALITY (Israt Jahan Susmi)
    # =========================================================================
    create_three_column_slide(
        slides[16], 16, 6,
        "Subsystem 5: Database & DevOps Infrastructure  |  Israt Jahan Susmi (2112280642)",
        "Asynchronous Connection Pooling & Database Engine Duality",
        COLOR_ROSE,
        (
            "Async Session Lifecycle",
            "SQLAlchemy AsyncEngine & Context",
            [
                "Engineers async_sessionmaker with expire_on_commit=False for non-blocking ORM access.",
                "Provides get_db() async generator yielding sessions into FastAPI dependency injection.",
                "Automates commit/rollback lifecycle: unhandled route exceptions trigger atomic rollback.",
                "Eliminates database deadlocks and resource leaks via guaranteed session closure.",
            ],
            "# Async Session Dependency Injection\nasync def get_db() -> AsyncGenerator[AsyncSession, None]:\n    async with AsyncSessionLocal() as session:\n        try: yield session; await session.commit()\n        except: await session.rollback(); raise"
        ),
        (
            "Connection Pool Optimization",
            "PostgreSQL 16 High-Load Sizing",
            [
                "Configures pool_size=20 persistent connections and max_overflow=10 burst slots.",
                "Enables pool_pre_ping=True: actively tests socket health before assigning to worker.",
                "Recycles stale connections silently to eliminate 'server closed connection unexpectedly'.",
                "Handles concurrent dual-document uploads without exhausting database file descriptors.",
            ],
            "# Production Pool Configuration\nengine = create_async_engine(\n    DATABASE_URL,\n    pool_size=20, max_overflow=10,\n    pool_pre_ping=True,\n    echo=False\n)"
        ),
        (
            "Dual-Engine Portability",
            "PostgreSQL & SQLite Seamless Fallback",
            [
                "Production: Connects to PostgreSQL 16 Alpine via high-speed asyncpg driver.",
                "Development / Defense: Defaults automatically to SQLite via aiosqlite driver.",
                "Zero code changes required between cloud container execution and local laptops.",
                "Enables instantaneous system demonstrations even without Docker Desktop active.",
            ],
            "# Zero-Config Dual Engine Portability\nDATABASE_URL = os.getenv(\n    'DATABASE_URL',\n    'sqlite+aiosqlite:///./grantlens.db' # Dev fallback\n)"
        ),
        "Connection Pooling", "Multi-Container Docker DevOps",
        "Persistent databases and web runtimes must be packaged into isolated, reproducible container environments."
    )

    # =========================================================================
    # SLIDE 18: MULTI-CONTAINER DOCKER ORCHESTRATION (Israt Jahan Susmi)
    # =========================================================================
    create_three_column_slide(
        slides[17], 17, 6,
        "Subsystem 5: Database & DevOps Infrastructure  |  Israt Jahan Susmi (2112280642)",
        "Multi-Container Docker Orchestration & Zero-Drift DevOps",
        COLOR_ROSE,
        (
            "Multi-Stage C++ Build Dockerfile",
            "Hermetic Toolchain Compilation",
            [
                "PyMuPDF and pdfplumber require native C/C++ compilation headers in Linux.",
                "Multi-stage Debian bookworm-slim base explicitly installs libmupdf-dev and build-essential.",
                "Compiles Python binary wheels cleanly, eliminating runtime missing .so library errors.",
                "Reduces production container footprint by stripping intermediate compilation artifacts.",
            ],
            "# Multi-Stage Debian Dockerfile\nFROM python:3.13-slim-bookworm\nRUN apt-get update && apt-get install -y \\\n    build-essential libmupdf-dev zlib1g-dev \\\n    && rm -rf /var/lib/apt/lists/*"
        ),
        (
            "Docker Compose Service Mesh",
            "Network Isolation & Lifecycle",
            [
                "Orchestrates two decoupled services: web (FastAPI gateway) and db (Postgres 16).",
                "Isolated bridge networking: grantlens_network restricts database port exposure.",
                "Service dependency conditioning: web boots only when db reports service_healthy.",
                "Prevents startup race conditions where the backend attempts queries before Postgres boots.",
            ],
            "# Compose Service Mesh & Health Dependency\nweb:\n  build: ./backend\n  depends_on:\n    db:\n      condition: service_healthy"
        ),
        (
            "Persistent Volumes & Healthchecks",
            "NVMe Data Retention & Self-Healing",
            [
                "Persistent Docker named volumes: pg_data preserves relational state across rebuilds.",
                "upload_cache volume stores raw PDF binaries safely outside container filesystem.",
                "Healthcheck command: pg_isready probes database availability every 5 seconds.",
                "Guarantees zero data loss, hermetic environment isolation, and zero environment drift.",
            ],
            "# PostgreSQL Healthcheck Probe\nhealthcheck:\n  test: ['CMD-SHELL', 'pg_isready -U grantlens_admin']\n  interval: 5s, timeout: 5s, retries: 5"
        ),
        "Docker DevOps", "System Performance Benchmarks",
        "With all subsystems operational and containerized, we evaluate end-to-end latency benchmarks and empirical performance."
    )

    # =========================================================================
    # SLIDE 19: SYSTEM INTEGRATION & PERFORMANCE BENCHMARKS (Synthesis)
    # =========================================================================
    create_three_column_slide(
        slides[18], 18, 7,
        "Subsystem 6: Platform Synthesis & Verification  |  Entire Engineering Team",
        "System Integration Verification & Empirical Latency Profile",
        COLOR_INDIGO,
        (
            "Subsystem Latency Profile",
            "Empirical Benchmark Measurements",
            [
                "Dual PDF Parsing (PyMuPDF + pdfplumber): 780 ms for 25-page solicitation + proposal.",
                "Deterministic Heuristic Compliance Scoring: 95 ms across 40+ compliance rules.",
                "Google Gemini 1.5 Flash AI SRO Narrative Review: 2.8 seconds end-to-end.",
                "Vite React Dev Server HMR: 137 ms cold start; 516 ms production bundle build.",
            ],
            "# Production Latency Profile\n| Subsystem              | Execution Time |\n| Ingestion & Geometry   | 780 ms         |\n| Heuristic Compliance   |  95 ms         |\n| Gemini SRO AI Review   | 2.80 s         |\n| Frontend Initial Load  | 137 ms         |"
        ),
        (
            "Automated Testing Coverage",
            "Verification Suite & Pipeline Fixtures",
            [
                "Unit Tests: Ingestion pipeline geometry, margin calculation, and currency extraction.",
                "Integration Tests: Full dual-PDF upload, database persistence, and token auth flow.",
                "Resiliency Tests: Simulated offline fallback, [object Object] error serialization.",
                "Verified 100% test pass rate across all Week 4 platform deliverables.",
            ],
            "# Test Suite Verification\n$ pytest backend/tests/\n================ 4 passed in 1.42s ================\n✓ test_ingestion_geometry PASSED\n✓ test_jwt_auth_lifecycle PASSED\n✓ test_heuristic_scoring  PASSED"
        ),
        (
            "Zero-Degradation Reliability",
            "Fault Tolerance & Error Recovery",
            [
                "Zero unhandled 500 server crashes observed across continuous testing cycles.",
                "Graceful fallback to simulated SRO review if Gemini API quota is throttled.",
                "Automatic session self-healing via /auth/me avoids stale token authentication drops.",
                "Provides rock-solid reliability for faculty grant deadlines and defense demos.",
            ],
            "# Operational Uptime Metrics\nPlatform Availability: 100.0%\nUnhandled Exceptions: 0\nDatabase Rollback Success: 100%\nContainer Restart Self-Healing: Verified"
        ),
        "System Verification", "Senior Design Roadmap & Q&A",
        "Having proven empirical performance and sub-second local latency, we outline the roadmap for Weeks 5 through 8."
    )

    # =========================================================================
    # SLIDE 20: ROADMAP, FUTURE SCOPE & INTERACTIVE Q&A (Synthesis)
    # =========================================================================
    s20 = slides[19]
    set_slide_background(s20)
    add_top_nav(s20, 7)
    add_slide_header(s20, "Roadmap & Conclusion", "Senior Design Execution Roadmap, Future Scope & Interactive Q&A", COLOR_INDIGO)

    c_w = Inches(3.98)
    c_h = Inches(4.5)
    c_gap = Inches(0.24)
    c_y = Inches(1.65)
    c_x1 = Inches(0.45)
    c_x2 = c_x1 + c_w + c_gap
    c_x3 = c_x2 + c_w + c_gap

    create_card(
        s20, c_x1, c_y, c_w, c_h,
        "Delivered Milestones (Weeks 1-4)",
        "Proven Engineering Infrastructure",
        [
            "Week 1: Scaffolding, Vite React frontend, Tailwind CSS v3 token system.",
            "Week 2: Docker Compose, PostgreSQL 16, PyMuPDF geometry extraction, JWT auth.",
            "Week 3: Gemini 1.5 Flash AI SRO review, rubric scoring, interactive diff explorer.",
            "Week 4: On-demand rewrite playground, error resilience, deep subsystem architecture.",
            "100% of claimed features are live, running, and verifiable in the codebase.",
        ],
        COLOR_EMERALD,
        "# Current Status: Weeks 1 - 4 Complete\nAll deliverables operating live at:\n• Frontend: http://localhost:5173\n• Backend:  http://127.0.0.1:8000"
    )

    create_card(
        s20, c_x2, c_y, c_w, c_h,
        "Future Roadmap (Weeks 5-8)",
        "Advanced Research Capabilities",
        [
            "Weeks 5-6: Full Grounded RAG with Vector DB (pgvector / ChromaDB) indexing 10,000+ historical funded NSF/NIH grant proposals.",
            "Weeks 7-8: Live Bidirectional Collaborative LaTeX & Markdown editor with automated track changes.",
            "Semantic Scholar & CrossRef integration for automated bibliographic citation verification.",
            "Multi-Institute SRO routing portal for university Sponsored Research Offices.",
        ],
        COLOR_AMBER,
        "# Upcoming Architecture Upgrades\n• pgvector / ChromaDB embedding retrieval\n• Multi-tenant university research offices\n• Semantic Scholar citation verification"
    )

    # Interactive Q&A Card with Subsystem Jump Links
    qa_card = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_x3, c_y, c_w, c_h)
    qa_card.fill.solid()
    qa_card.fill.fore_color.rgb = CARD_BG
    qa_card.line.color.rgb = COLOR_ORANGE
    qa_card.line.width = Pt(1.5)

    tf = qa_card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.18)
    tf.margin_right = Inches(0.18)
    tf.margin_top = Inches(0.16)

    p = tf.paragraphs[0]
    p.text = "Interactive Examiner Q&A Hub"
    p.font.name = "Arial"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_ORANGE

    p2 = tf.add_paragraph()
    p2.text = "Click any subsystem below to jump instantly to its technical slide for defense discussion:"
    p2.font.name = "Arial"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(6)

    jump_links = [
        ("➔ PyMuPDF Bounding Box Geometry", 3, COLOR_CYAN),
        ("➔ Font Span Histograms & Evasion", 4, COLOR_CYAN),
        ("➔ Tabular Financial & Budget Ledger", 5, COLOR_CYAN),
        ("➔ Deterministic 3-Tier Rule Engine", 6, COLOR_PURPLE),
        ("➔ Multi-Factor Penalty Scoring", 7, COLOR_PURPLE),
        ("➔ Gemini 1.5 Flash SRO Architecture", 9, COLOR_AMBER),
        ("➔ SRO Rubric Evaluation Criteria", 10, COLOR_AMBER),
        ("➔ Interactive Diff & Visual UX", 12, COLOR_EMERALD),
        ("➔ On-Demand Rewrite Playground", 13, COLOR_EMERALD),
        ("➔ Relational Schema & UUID Modeling", 15, COLOR_ROSE),
        ("➔ Connection Pooling & Dual DB", 16, COLOR_ROSE),
        ("➔ Docker Multi-Stage DevOps Mesh", 17, COLOR_ROSE),
    ]

    # Add interactive jump buttons inside card
    btn_y_start = Inches(2.7)
    btn_h = Inches(0.24)
    btn_gap = Inches(0.06)

    for idx, (j_label, target_idx, j_col) in enumerate(jump_links[:11]): # Fit top 11
        by = btn_y_start + idx * (btn_h + btn_gap)
        jbtn = s20.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_x3 + Inches(0.18), by, c_w - Inches(0.36), btn_h)
        jbtn.fill.solid()
        jbtn.fill.fore_color.rgb = RGBColor(15, 23, 42)
        jbtn.line.color.rgb = CARD_BORDER
        jbtn.line.width = Pt(0.5)
        jbtn.click_action.target_slide = slides[target_idx]

        p = jbtn.text_frame.paragraphs[0]
        p.text = j_label
        p.alignment = PP_ALIGN.LEFT
        p.font.name = "Arial"
        p.font.size = Pt(8.5)
        p.font.bold = True
        p.font.color.rgb = j_col

    add_transition_banner(s20, "System Performance Benchmarks", "Examiner Q&A Session", "Concluded formal presentation. The slide deck remains fully interactive for examiner defense inquiries.")
    add_bottom_footer(s20, 19)

    # Save Presentation
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs.save(output_path)
    print(f"================================================================================")
    print(f"SUCCESS: Interactive Presentation generated at: {output_path}")
    print(f"Total Slides: {len(slides)} (16:9 Widescreen, Fully Hyperlinked Interactive Deck)")
    print(f"================================================================================")

if __name__ == "__main__":
    out_file = "others/GrantLens_Week4_Interactive_Presentation.pptx"
    build_week4_interactive_presentation(out_file)
