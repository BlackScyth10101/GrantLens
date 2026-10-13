"""
GrantLens - Weekly Progress Report Generator
Output: d:/GrantLens/GrantLens_Week1_Progress_Report.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, ListFlowable, ListItem
)

DARK      = colors.HexColor('#1a1a1a')
BLUE_LINK = colors.HexColor('#1155CC')
ORANGE    = colors.HexColor('#E67E00')
TEAL      = colors.HexColor('#0070C0')
BLACK     = colors.black
GRAY      = colors.HexColor('#555555')
TBL_HEAD  = colors.HexColor('#f2f2f2')
TBL_BDR   = colors.HexColor('#cccccc')
LINE_C    = colors.HexColor('#333333')

def S(name, **kw):
    base = dict(fontName='Helvetica', fontSize=10.5, leading=14,
                textColor=DARK, spaceAfter=2, spaceBefore=0, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)

TITLE_S  = S('title',  fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=BLACK, spaceAfter=3)
SUB_S    = S('sub',    fontName='Helvetica', fontSize=10.5, leading=14, textColor=DARK, spaceAfter=2)
BOLD_S   = S('bold',   fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=BLACK, spaceAfter=2)
SEC_S    = S('sec',    fontName='Helvetica-Bold', fontSize=12.5, leading=16, textColor=BLACK, spaceBefore=12, spaceAfter=4)
SUBSEC_S = S('subsec', fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=TEAL, spaceBefore=8, spaceAfter=4)
BODY_S   = S('body',   fontName='Helvetica', fontSize=10.5, leading=14, textColor=DARK, spaceAfter=3, alignment=TA_JUSTIFY)
TBL_HD_S = S('tblhd',  fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=BLACK)
TBL_B_S  = S('tblb',   fontName='Helvetica', fontSize=10.5, leading=14, textColor=DARK)
SIG_S    = S('sig',    fontName='Helvetica', fontSize=10.5, leading=14, textColor=DARK, spaceAfter=4, spaceBefore=6)

def sp(h=6):   return Spacer(1, h)
def rule():    return HRFlowable(width='100%', thickness=0.7, color=LINE_C, spaceAfter=6, spaceBefore=4)
def body(t):   return Paragraph(t, BODY_S)
def bold(t):   return Paragraph(t, BOLD_S)

def sub_bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, BODY_S), bulletColor=GRAY) for i in items],
        bulletType='bullet', start='o', leftIndent=40, bulletFontSize=9, bulletOffsetY=-1
    )

def build():
    out = r'd:\GrantLens\GrantLens_Week1_Progress_Report.pdf'
    doc = SimpleDocTemplate(out, pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.5*cm,
        topMargin=2.2*cm, bottomMargin=2.2*cm,
        title='Week 1 Progress Report: GrantLens')

    usable = doc.width
    story  = []

    # ── PAGE 1 ──────────────────────────────────────────────────────────────────
    story.append(Paragraph('Weekly Progress Report: GrantLens', TITLE_S))
    story.append(Paragraph('Course Code : CSE299  |  Sec : 3', SUB_S))
    story.append(sp(2))
    story.append(Paragraph('Project Group No: 3', SUB_S))
    story.append(Paragraph('<b>Group Members:</b>', BOLD_S))

    members = [
        ('Anas Ibne Majbha',  '2322846642'),
        ('Tazreen Alam',      '2321506042'),
        ('Hasin Anzum Inan',  '2323133042'),
        ('Israt Jahan Susmi', '2112280642'),
    ]
    for name, sid in members:
        story.append(Paragraph(
            '<font color="#1155CC">{} ({})</font>'.format(name, sid), SUB_S))

    story.append(sp(10))
    story.append(rule())
    story.append(sp(6))

    story.append(Paragraph('Week 1: Project Setup &amp; Planning', SEC_S))
    story.append(sp(2))
    story.append(body('<b>Sprint Goal:</b> Project setup, repository scaffolding, '
                      'initial UI architecture, and full-stack frontend-to-backend '
                      'API connection.'))
    story.append(sp(10))
    story.append(Paragraph('Planned Objectives', SUBSEC_S))

    col1 = usable * 0.30
    col2 = usable * 0.24
    col3 = usable * 0.46

    def cell(text, style=TBL_B_S):
        return Paragraph(text, style)

    def member_cell(name, sid):
        nt = Table([
            [Paragraph('<font color="#1155CC">{}</font>'.format(name), TBL_B_S)],
            [Paragraph('<font color="#E67E00">ID: {}</font>'.format(sid),
                       ParagraphStyle('ids', fontName='Helvetica', fontSize=9.5,
                                      leading=12, textColor=ORANGE))],
        ], colWidths=[col1 - 12])
        nt.setStyle(TableStyle([
            ('TOPPADDING',    (0,0),(-1,-1), 0),
            ('BOTTOMPADDING', (0,0),(-1,-1), 1),
            ('LEFTPADDING',   (0,0),(-1,-1), 0),
            ('RIGHTPADDING',  (0,0),(-1,-1), 0),
        ]))
        return nt

    tbl_data = [
        # Header
        [cell('Member', TBL_HD_S), cell('Role', TBL_HD_S), cell('Weekly Objectives', TBL_HD_S)],

        # Anas — Backend
        [member_cell('Anas Ibne Majbha', '2322846642'),
         cell('Backend'),
         cell('Django 6.1 project scaffold, Django REST Framework (DRF) setup, '
              'database initialisation (db.sqlite3 via migrations), /api/status/ '
              'endpoint returning live JSON telemetry.')],

        # Tazreen — FE UI
        [member_cell('Tazreen Alam', '2321506042'),
         cell('FE - UI / Integration'),
         cell('Landing page UI design, interactive metric dashboard cards, '
              'React state management (useState, useEffect), dynamic API data '
              'binding, status badge and upload dropzone layout.')],

        # Hasin — FE Core + AI/Tech Lead
        [member_cell('Hasin Anzum Inan', '2323133042'),
         cell('FE Core & AI / Tech Lead'),
         cell('Vite + React scaffolding, Tailwind CSS design system (brand & navy '
              'tokens), Lucide icons, overall system architecture, CORS handshake '
              'resolution, PRD & compliance rule schema, upcoming tool scoping '
              '(PyMuPDF, ChromaDB, Gemini API).')],

        # Israt — Project Setup
        [member_cell('Israt Jahan Susmi', '2112280642'),
         cell('Project Setup'),
         cell('GitHub repository creation and configuration, initial project '
              'folder structure, dependency documentation (requirements.txt, '
              'package.json), README drafting, team onboarding support.')],
    ]

    tbl = Table(tbl_data, colWidths=[col1, col2, col3])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0, 0), (-1, 0), TBL_HEAD),
        ('FONTNAME',      (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID',          (0, 0), (-1, -1), 0.5, TBL_BDR),
        ('VALIGN',        (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING',    (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING',   (0, 0), (-1, -1), 6),
        ('RIGHTPADDING',  (0, 0), (-1, -1), 6),
        ('FONTSIZE',      (0, 0), (-1, -1), 10.5),
        ('LEADING',       (0, 0), (-1, -1), 14),
    ]))
    story.append(tbl)

    # ── PAGE 2 ──────────────────────────────────────────────────────────────────
    story.append(sp(18))
    story.append(rule())
    story.append(sp(6))

    story.append(Paragraph('Progress Summary', SEC_S))
    story.append(sp(2))

    story.append(bold('Work Completed:'))
    story.append(sub_bullets([
        'GitHub repository created at github.com/BlackScyth10101/GrantLens — all 44 files committed.',
        'Vite + React 18 frontend scaffolded and running at localhost:5173.',
        'Tailwind CSS v3 design system configured with custom brand/navy colour tokens.',
        'Django 6.1 + DRF backend running at localhost:8000.',
        'SQLite database initialised via python manage.py migrate.',
        'CORS fully resolved — django-cors-headers with CorsMiddleware at index 0.',
        '/api/status/ endpoint returns live JSON with timestamp, metrics, and status.',
        'React useState + useEffect + fetch() pipeline verified end-to-end.',
        '4 live metric tiles and status badge bind directly to Django API data.',
        'Production Vite build passes in 341 ms with zero errors.',
    ]))
    story.append(sp(6))

    story.append(bold('Challenges Encountered:'))
    story.append(sub_bullets([
        'Tailwind CSS v4 altered its PostCSS plugin API — build pipeline broke on install.',
        'CORS block: Browser rejected all fetch() calls from port 5173 to port 8000.',
        'Infinite render loop: Missing [] in useEffect caused endless network requests.',
        'lucide-react: Github icon not exported from the package — caused build error.',
    ]))
    story.append(sp(6))

    story.append(bold('Proposed Solutions:'))
    story.append(sub_bullets([
        'Pinned tailwindcss@^3.4.17 in package.json — v3 uses the correct CommonJS PostCSS format.',
        'Added django-cors-headers and placed CorsMiddleware at index 0 of MIDDLEWARE. '
        'Set CORS_ALLOW_ALL_ORIGINS = True for development.',
        'Added empty dependency array [] as second argument to useEffect — restricts '
        'execution to once on component mount only.',
        'Removed unused Github icon import from lucide-react entirely.',
    ]))
    story.append(sp(6))

    story.append(bold('Overall Status:'))
    story.append(sub_bullets([
        'All Week 1 milestone objectives achieved. Repository setup, frontend-backend '
        'connection, and live data binding are fully operational.',
    ]))
    story.append(sp(14))

    story.append(Paragraph('Detailed Weekly Log', SUBSEC_S))
    story.append(sp(4))

    story.append(body(
        'After coordinating across four workstreams, the team successfully integrated a fully '
        'functional full-stack web application within the Week 1 sprint. All dependencies were '
        'installed, a shared GitHub repository was established, and the project was verified '
        'running on each team member\'s local machine.'
    ))
    story.append(sp(4))

    log_entries = [
        ('Member 1: Anas Ibne Majbha',
         'built the Django 6.1 backend — scaffolded the Django project, installed Django REST '
         'Framework, and implemented the /api/status/ API endpoint using the @api_view decorator '
         'and DRF Response class. Ran database migrations to initialise SQLite and verified '
         'the API returns correct JSON with a live timestamp.'),

        ('Member 2: Tazreen Alam',
         'designed and implemented the frontend UI — built the single-page layout including '
         'the Navbar, Hero section, 4 metric dashboard cards, and upload dropzone. Implemented '
         'React state management using useState and useEffect, and connected the fetch() API '
         'pipeline to display live data from the Django backend.'),

        ('Member 3: Hasin Anzum Inan',
         'led the frontend core setup and served as AI/Tech Lead — initialised the Vite + React '
         'project, configured Tailwind CSS v3 with custom brand colour tokens, resolved the '
         'CORS handshake by configuring django-cors-headers correctly, and finalised the overall '
         'system architecture. Also drafted the Product Requirements Document (PRD) and scoped '
         'the Week 2 AI toolchain (PyMuPDF, ChromaDB, Google Gemini API).'),

        ('Member 4: Israt Jahan Susmi',
         'handled initial project setup — created and configured the GitHub repository, '
         'defined the project folder structure, set up requirements.txt and package.json '
         'dependency documentation, wrote the README, and helped onboard the rest of the '
         'team to the shared codebase.'),
    ]

    for label, text in log_entries:
        story.append(Paragraph('<b>{}</b> {}'.format(label, text), BODY_S))
        story.append(sp(3))

    story.append(sp(16))
    story.append(Paragraph('Report Date: October 2026', SIG_S))
    story.append(Paragraph('Supervisor Signature: __________________________', SIG_S))
    story.append(sp(10))
    story.append(rule())

    doc.build(story)
    print("DONE! Saved:", out)

build()
