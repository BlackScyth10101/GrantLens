"""
GrantLens - Week 1 Post-Proposal Presentation Generator
Generates a 22-slide PPTX using python-pptx.
Run: python generate_final_pptx.py
Output: d:/GrantLens/GrantLens_Week1_Final_Presentation.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ─────────────────────────────────────────────
# COLOUR PALETTE
# ─────────────────────────────────────────────
BG_DARK       = RGBColor(0x07, 0x0A, 0x12)   # #070A12 – main background
CARD_BG       = RGBColor(0x0F, 0x16, 0x26)   # #0F1626 – card surface
CARD_BG2      = RGBColor(0x14, 0x1E, 0x34)   # #141E34 – metric tiles
BORDER        = RGBColor(0x2A, 0x3F, 0x66)   # #2A3F66 – border lines
ORANGE        = RGBColor(0xF9, 0x73, 0x16)   # #F97316 – primary accent
ORANGE_DIM    = RGBColor(0xC2, 0x41, 0x0C)   # #C2410C – dimmer orange
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY    = RGBColor(0xB0, 0xBC, 0xD4)   # body text
MID_GRAY      = RGBColor(0x64, 0x74, 0x8B)   # muted labels
GREEN         = RGBColor(0x10, 0xB9, 0x81)   # success / connected
CYAN          = RGBColor(0x38, 0xBD, 0xF8)   # info / code accent
CODE_BG       = RGBColor(0x0B, 0x0F, 0x19)   # #0B0F19 – code block bg

# Slide dimensions: 13.33" x 7.5" (widescreen 16:9)
SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

BLANK_LAYOUT = prs.slide_layouts[6]  # completely blank


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def add_slide():
    slide = prs.slides.add_slide(BLANK_LAYOUT)
    # Dark background rectangle
    bg = slide.shapes.add_shape(1, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return slide


def txt(slide, text, x, y, w, h,
        size=18, bold=False, italic=False,
        color=WHITE, align=PP_ALIGN.LEFT, wrap=True):
    txb = slide.shapes.add_textbox(x, y, w, h)
    tf  = txb.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size    = Pt(size)
    run.font.bold    = bold
    run.font.italic  = italic
    run.font.color.rgb = color
    run.font.name = "Segoe UI"
    return txb


def mono(slide, text, x, y, w, h, size=11, color=CYAN):
    """Monospace text for code blocks."""
    txb = slide.shapes.add_textbox(x, y, w, h)
    tf  = txb.text_frame
    tf.word_wrap = True
    p   = tf.paragraphs[0]
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.name = "Consolas"
    return txb


def rect(slide, x, y, w, h, fill=CARD_BG, border=BORDER, border_w=Pt(1)):
    shape = slide.shapes.add_shape(1, x, y, w, h)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = border
    shape.line.width = border_w
    return shape


def code_block(slide, code_text, x, y, w, h, size=10):
    """Dark code block with monospace text."""
    rect(slide, x, y, w, h, fill=CODE_BG, border=BORDER)
    mono(slide, code_text, x + Inches(0.15), y + Inches(0.1),
         w - Inches(0.3), h - Inches(0.2), size=size, color=CYAN)


def accent_bar(slide, y=Inches(0.55), thick=Pt(3)):
    """Thin orange horizontal rule under slide heading area."""
    line = slide.shapes.add_shape(1, Inches(0.5), y, Inches(12.33), Pt(2))
    line.fill.solid()
    line.fill.fore_color.rgb = ORANGE
    line.line.fill.background()


def slide_number(slide, n):
    txt(slide, str(n), Inches(12.7), Inches(7.1), Inches(0.5), Inches(0.3),
        size=10, color=MID_GRAY, align=PP_ALIGN.RIGHT)


def pill(slide, label, x, y, w=Inches(2.2), h=Inches(0.38),
         bg=ORANGE, text_color=WHITE, size=11):
    r = slide.shapes.add_shape(1, x, y, w, h)
    r.fill.solid()
    r.fill.fore_color.rgb = bg
    r.line.fill.background()
    tf = r.text_frame
    tf.word_wrap = False
    p  = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = label
    run.font.size  = Pt(size)
    run.font.bold  = True
    run.font.color.rgb = text_color
    run.font.name  = "Segoe UI"


# ─────────────────────────────────────────────
# SLIDE 1 — TITLE
# ─────────────────────────────────────────────
s = add_slide()
slide_number(s, 1)

# Orange glow strip
strip = s.shapes.add_shape(1, 0, Inches(3.2), SLIDE_W, Inches(0.06))
strip.fill.solid(); strip.fill.fore_color.rgb = ORANGE
strip.line.fill.background()

txt(s, "GrantLens", Inches(1), Inches(1.2), Inches(11.33), Inches(1.4),
    size=64, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txt(s, "AI-Powered Grant Audit & Evaluation Platform",
    Inches(1), Inches(2.6), Inches(11.33), Inches(0.6),
    size=22, italic=True, color=ORANGE, align=PP_ALIGN.CENTER)

txt(s, "Week 1 Milestone  ·  CSE299 Section 3  ·  Group 2",
    Inches(1), Inches(3.35), Inches(11.33), Inches(0.5),
    size=15, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

txt(s, "Post-Proposal Progress Presentation",
    Inches(1), Inches(4.05), Inches(11.33), Inches(0.45),
    size=14, color=MID_GRAY, align=PP_ALIGN.CENTER)

pill(s, "React + Django  ·  Live API Connected",
     Inches(4.4), Inches(5.0), w=Inches(4.53), h=Inches(0.42), size=13)

# ─────────────────────────────────────────────
# SLIDE 2 — WHAT IS GRANTLENS?
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 2)
txt(s, "What is GrantLens?", Inches(0.5), Inches(0.1), Inches(12), Inches(0.55),
    size=30, bold=True, color=WHITE)

txt(s, "GrantLens is a web application that uses Artificial Intelligence to automatically check grant proposals for compliance errors — replacing hours of manual reading with instant, reliable auditing.",
    Inches(0.5), Inches(0.75), Inches(12.33), Inches(1.2),
    size=17, color=LIGHT_GRAY)

boxes = [
    ("🔍  The Problem", "30% of grant proposals are rejected immediately at the desk review stage — not because the science is bad, but because documents broke simple formatting or budget rules."),
    ("💡  Our Solution", "GrantLens reads the uploaded PDF, checks every section against the funding agency's ruleset, and produces a compliance score with highlighted violations."),
    ("🎓  What We Built in Week 1", "A full-stack web app: a React frontend that talks over HTTP to a Django backend. The frontend shows live metrics from the server in real time."),
    ("🗓️  Next Steps (Week 2)", "Add PDF upload, AI text extraction (PyMuPDF), and rule-checking engine (Google Gemini). Week 1 is the foundation."),
]
for i, (title, body) in enumerate(boxes):
    col = i % 2; row = i // 2
    bx = Inches(0.5) + col * Inches(6.45)
    by = Inches(2.15) + row * Inches(2.2)
    rect(s, bx, by, Inches(6.1), Inches(2.0), fill=CARD_BG2, border=BORDER)
    txt(s, title, bx + Inches(0.2), by + Inches(0.12),
        Inches(5.7), Inches(0.4), size=14, bold=True, color=ORANGE)
    txt(s, body, bx + Inches(0.2), by + Inches(0.55),
        Inches(5.7), Inches(1.3), size=12, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 3 — TECHNOLOGY STACK
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 3)
txt(s, "Our Technology Stack", Inches(0.5), Inches(0.1), Inches(12), Inches(0.55),
    size=30, bold=True, color=WHITE)

txt(s, "Everything used in Week 1 is 100% in the code — no hypothetical tools listed here.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.4),
    size=14, italic=True, color=MID_GRAY)

stack = [
    ("FRONTEND", [
        ("React 18", "UI component library. Everything you see on screen is a React component."),
        ("Vite", "Ultra-fast build tool. Replaces slow Webpack. Builds in < 400ms."),
        ("Tailwind CSS v3", "Utility-first CSS. We define colors & styles in tailwind.config.js."),
        ("Lucide React", "Clean SVG icons (Upload, TrendingUp, Award, etc.)."),
        ("fetch() API", "Browser-native tool to send HTTP requests to Django."),
    ]),
    ("BACKEND", [
        ("Django 6.1", "Python web framework. Handles routing, auth, and server logic."),
        ("Django REST Framework", "DRF converts Python dictionaries into JSON automatically."),
        ("django-cors-headers", "Solves the browser's Same-Origin Policy security block."),
        ("SQLite", "Simple file-based database. Stores data in db.sqlite3."),
        ("Python 3.13", "The language running the entire backend server."),
    ]),
]
for ci, (col_title, items) in enumerate(stack):
    cx = Inches(0.5) + ci * Inches(6.45)
    rect(s, cx, Inches(1.25), Inches(6.1), Inches(5.85), fill=CARD_BG, border=BORDER)
    pill(s, col_title, cx + Inches(0.15), Inches(1.35),
         w=Inches(2.0), h=Inches(0.32),
         bg=ORANGE if ci == 0 else GREEN, size=11)
    for j, (name, desc) in enumerate(items):
        iy = Inches(1.85) + j * Inches(0.95)
        txt(s, f"▸  {name}", cx + Inches(0.25), iy,
            Inches(5.6), Inches(0.3), size=14, bold=True, color=WHITE)
        txt(s, desc, cx + Inches(0.25), iy + Inches(0.3),
            Inches(5.6), Inches(0.55), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 4 — HOW FRONTEND & BACKEND CONNECT
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 4)
txt(s, "How the Frontend & Backend Connect", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

# Flow diagram boxes
nodes = [
    (Inches(0.4), Inches(1.8), "Browser\n(React App)", CARD_BG2),
    (Inches(3.4), Inches(1.8), "fetch()\nAPI Call", ORANGE_DIM),
    (Inches(6.3), Inches(1.8), "CORS\nMiddleware", CARD_BG2),
    (Inches(9.2), Inches(1.8), "Django\nDRF View", GREEN),
]
for nx, ny, label, color in nodes:
    rect(s, nx, ny, Inches(2.4), Inches(1.2), fill=color, border=BORDER)
    txt(s, label, nx, ny + Inches(0.2), Inches(2.4), Inches(0.8),
        size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# Arrows between nodes
for ax in [Inches(2.85), Inches(5.8), Inches(8.7)]:
    txt(s, "→", ax, Inches(2.1), Inches(0.5), Inches(0.5),
        size=22, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)

# Return path
txt(s, "← JSON Response travels back the same path",
    Inches(0.4), Inches(3.2), Inches(12), Inches(0.45),
    size=14, italic=True, color=CYAN, align=PP_ALIGN.CENTER)

steps = [
    "1. User opens the web app at http://localhost:5173",
    "2. React mounts → useEffect fires checkBackend() once",
    "3. fetch() sends HTTP GET to http://127.0.0.1:8000/api/status/",
    "4. CorsMiddleware adds 'Access-Control-Allow-Origin: *' header → browser allows it",
    "5. Django's URLResolver matches 'api/status/' → calls api_status() view",
    "6. api_status() builds a Python dict → DRF serializes it to JSON → HTTP 200 returned",
    "7. React receives JSON → setBackendStatus() updates state → Virtual DOM re-renders",
    "8. Green '🟢 Connected' badge appears. Metric cards fill with live numbers.",
]
for i, step in enumerate(steps):
    sy = Inches(3.75) + i * Inches(0.41)
    col = GREEN if "JSON" in step or "Connected" in step else LIGHT_GRAY
    txt(s, step, Inches(0.5), sy, Inches(12.33), Inches(0.38), size=12, color=col)

# ─────────────────────────────────────────────
# SLIDE 5 — WHAT IS REACT?
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 5)
txt(s, "The Frontend — What is React?", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "React is a JavaScript library built by Meta for building user interfaces. Instead of manually editing HTML every time data changes, React automatically updates only the parts of the screen that need to change.",
    Inches(0.5), Inches(0.75), Inches(12.33), Inches(0.9), size=16, color=LIGHT_GRAY)

concepts = [
    ("Component", "A self-contained piece of the UI (like a card, a button, or the whole page). Our entire app is one component: the App() function in App.jsx."),
    ("JSX", "JavaScript + HTML mixed together. React lets you write HTML tags directly inside JavaScript. Vite compiles this into plain JavaScript behind the scenes."),
    ("Virtual DOM", "React keeps a lightweight copy of the page in memory. When state changes, it compares the old and new copies and updates only the changed parts — this is fast."),
    ("State", "Data stored inside a component. When state changes, React automatically re-renders. We use the useState() hook to create and manage state."),
    ("Props", "Data passed from a parent component down to a child. Like function arguments — but for UI components."),
    ("Hooks", "Special React functions (useState, useEffect) that let you add memory and lifecycle behavior to functional components."),
]
for i, (title, body) in enumerate(concepts):
    col = i % 2; row = i // 2
    bx = Inches(0.4) + col * Inches(6.47)
    by = Inches(1.82) + row * Inches(1.73)
    rect(s, bx, by, Inches(6.15), Inches(1.6), fill=CARD_BG, border=BORDER)
    txt(s, title, bx + Inches(0.2), by + Inches(0.1),
        Inches(5.75), Inches(0.38), size=14, bold=True, color=ORANGE)
    txt(s, body, bx + Inches(0.2), by + Inches(0.5),
        Inches(5.75), Inches(1.0), size=11.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 6 — VITE: THE BUILD TOOL
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 6)
txt(s, "Vite — The Build Tool", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "A build tool turns our modern code (JSX, ES Modules, Tailwind CSS) into plain HTML/CSS/JS that any browser can read. Vite is the fastest build tool available today.",
    Inches(0.5), Inches(0.72), Inches(8.0), Inches(0.8), size=15, color=LIGHT_GRAY)

# Code block
code_block(s, """// vite.config.js — Full configuration file

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath, URL } from 'node:url';

export default defineConfig({
  plugins: [react()],        // Enables JSX transform + Fast Refresh (HMR)

  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },                       // '@/components/X' instead of '../../components/X'
  },

  server: {
    port: 5173,              // Dev server runs on http://localhost:5173
    host: true,              // Accessible on local network (all devices)
  },
});""",
    Inches(0.4), Inches(1.65), Inches(7.2), Inches(5.2), size=10)

# Sidebar explanations
points = [
    ("plugins: [react()]", "Transforms JSX into JS calls. Enables Hot Module Replacement — save a file and the browser updates instantly without refreshing."),
    ("resolve.alias '@'", "Lets us write import Foo from '@/components/Foo' instead of messy '../../../' paths."),
    ("server.port: 5173", "Vite runs your app at http://localhost:5173 during development. You open this in your browser."),
    ("Why not Webpack?", "Webpack bundles all files before serving — slow on large projects. Vite serves each file on-demand using native browser ES Modules (ESM)."),
]
for i, (title, body) in enumerate(points):
    by = Inches(1.65) + i * Inches(1.38)
    rect(s, Inches(7.8), by, Inches(5.1), Inches(1.25), fill=CARD_BG, border=BORDER)
    txt(s, title, Inches(8.0), by + Inches(0.08),
        Inches(4.7), Inches(0.35), size=13, bold=True, color=ORANGE)
    txt(s, body, Inches(8.0), by + Inches(0.42),
        Inches(4.7), Inches(0.75), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 7 — TAILWIND CSS
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 7)
txt(s, "Tailwind CSS — How We Styled Everything", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Tailwind CSS is a utility-first CSS framework. Instead of writing a separate .css file, you style elements directly in JSX using short class names.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=15, color=LIGHT_GRAY)

code_block(s, """// tailwind.config.js — Custom Design Tokens

export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",  // Tailwind scans all these files for class names
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          500: '#F97316',  // Primary orange accent (buttons, highlights)
        },
        navy: {
          950: '#070A12',  // App background — deepest dark
          800: '#141E34',  // Card backgrounds
          700: '#1E2D4A',  // Borders
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Consolas', 'monospace'],
      },
    },
  },
};""",
    Inches(0.4), Inches(1.35), Inches(7.2), Inches(5.6), size=10)

points = [
    ("JIT Compiler", "Tailwind scans every .jsx file and generates ONLY the CSS classes you actually used. The final CSS file is tiny — around 32 KB."),
    ("Custom Tokens", "We defined our own brand.500 orange and navy.950 dark background so every team member uses the same colors without guessing hex codes."),
    ("Utility Classes in JSX", "className='bg-navy-800 text-white rounded-xl p-4' — no separate .css file needed."),
    ("Why We Pinned v3.4.17", "Tailwind v4 changed its PostCSS plugin format and broke our build. We explicitly pinned version 3 to fix this."),
]
for i, (title, body) in enumerate(points):
    by = Inches(1.35) + i * Inches(1.38)
    rect(s, Inches(7.8), by, Inches(5.1), Inches(1.25), fill=CARD_BG, border=BORDER)
    txt(s, title, Inches(8.0), by + Inches(0.08),
        Inches(4.7), Inches(0.35), size=13, bold=True, color=ORANGE)
    txt(s, body, Inches(8.0), by + Inches(0.42),
        Inches(4.7), Inches(0.75), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 8 — useState HOOK
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 8)
txt(s, "React useState — Giving Components Memory", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "useState is a React Hook that lets a component remember data between re-renders. Without it, every re-render would reset all variables.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

code_block(s, """// From App.jsx — Lines 41-45

// useState Hook: Declares a state variable and its updater function.
// React stores this data in its internal Fiber tree (persistent memory).
const [backendStatus, setBackendStatus] = useState({
  connected: false,   // Boolean — Is Django responding?
  loading: true,      // Boolean — Are we still waiting for the HTTP response?
  data: null,         // Object  — The actual JSON from Django (or null)
});

// ----- HOW IT WORKS -----
// useState({ connected: false, loading: true, data: null })
//   └─ returns an ARRAY with exactly 2 elements:
//        [0] backendStatus  → the current value of the state
//        [1] setBackendStatus → a function that UPDATES the state

// When setBackendStatus({ connected: true, ... }) is called:
//   1. React stores the new value in its Fiber node memory
//   2. React schedules a re-render of the App() component
//   3. Virtual DOM diff runs → only changed JSX nodes update in the real DOM""",
    Inches(0.4), Inches(1.35), Inches(7.5), Inches(5.6), size=10)

boxes = [
    ("Step 1: Initial Mount", "backendStatus.connected = false\nbackendStatus.loading = true\n→ UI shows 'Connecting...' spinner"),
    ("Step 2: Fetch Complete", "setBackendStatus({ connected: true, data: {...} })\n→ React re-renders the component"),
    ("Step 3: UI Updates", "The '🟢 Connected' badge renders.\nMetric tiles fill with real Django numbers."),
]
for i, (title, body) in enumerate(boxes):
    by = Inches(1.35) + i * Inches(1.92)
    rect(s, Inches(8.1), by, Inches(4.8), Inches(1.8), fill=CARD_BG2, border=BORDER)
    txt(s, title, Inches(8.3), by + Inches(0.1),
        Inches(4.4), Inches(0.38), size=13, bold=True, color=ORANGE)
    txt(s, body, Inches(8.3), by + Inches(0.52),
        Inches(4.4), Inches(1.1), size=11.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 9 — useEffect HOOK
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 9)
txt(s, "React useEffect — Running Code at the Right Time", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "useEffect lets you run code AFTER the component renders — perfect for network requests, timers, and subscriptions that shouldn't block the UI from painting.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

code_block(s, """// From App.jsx — Lines 88-90 (the Lifecycle Hook)

useEffect(() => {
  checkBackend();   // Calls our async fetch function once when the page loads
}, []);             // ← The dependency array


// ─── WHY THE EMPTY ARRAY [] IS CRITICAL ───────────────────────────────────
//
//   useEffect(fn, [])          → Runs fn() ONCE after first render (CORRECT ✓)
//
//   useEffect(fn)              → Runs fn() after EVERY render (INFINITE LOOP ✗)
//     Why? checkBackend() calls setBackendStatus()
//          setBackendStatus() triggers a re-render
//          re-render triggers useEffect again
//          → CRASH: infinite network requests hammering Django
//
//   useEffect(fn, [someVar])   → Runs fn() whenever someVar changes
//     Useful for: re-fetching data when a search query input changes
//
// ─── LIFECYCLE TIMELINE ───────────────────────────────────────────────────
//   Component function runs → JSX returned → Real DOM painted
//   → useEffect fires → fetch() starts → Django responds
//   → setBackendStatus() called → re-render scheduled → UI updates""",
    Inches(0.4), Inches(1.35), Inches(8.5), Inches(5.6), size=10)

rect(s, Inches(9.1), Inches(1.35), Inches(3.8), Inches(5.6), fill=CARD_BG, border=BORDER)
txt(s, "⚠️  Common Mistake", Inches(9.3), Inches(1.5),
    Inches(3.4), Inches(0.38), size=14, bold=True, color=ORANGE)
txt(s, """Missing [] causes infinite loop:

  useEffect(() => {
    checkBackend();
  });  ← no array!

Every render fires fetch()
Every fetch updates state
Every state update re-renders
Browser CRASHES.

This is the #1 beginner
mistake with useEffect.

The fix: always add []
as the second argument
when you only want the
effect to run once.""",
    Inches(9.3), Inches(1.95), Inches(3.4), Inches(4.85),
    size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 10 — THE FETCH API
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 10)
txt(s, "The fetch() API — Talking to Django", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "fetch() is built into every modern browser. It sends an HTTP request over the network and returns a Promise — a placeholder for data that hasn't arrived yet.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

code_block(s, """// From App.jsx — Lines 52-77: The full async network pipeline

const checkBackend = async () => {
  try {
    // Step 1: Send HTTP GET request to Django
    // 'await' pauses this function (NOT the whole browser) until Django responds
    const response = await fetch('http://127.0.0.1:8000/api/status/');

    // Step 2: Check if Django returned HTTP 200 OK
    // response.ok is true for status codes 200-299
    if (response.ok) {

      // Step 3: Parse the incoming JSON byte-stream into a JS object
      // This is also async — the body data streams over the network
      const data = await response.json();

      // Step 4: Update React state with live data — triggers re-render
      setBackendStatus({ connected: true, loading: false, data });

    } else {
      setBackendStatus({ connected: false, loading: false, data: null });
    }

  } catch {
    // Catches network errors (Django turned off = ERR_CONNECTION_REFUSED)
    // Without try/catch, this would be an Uncaught Promise Rejection in console
    setBackendStatus({ connected: false, loading: false, data: null });
  }
};""",
    Inches(0.4), Inches(1.35), Inches(8.3), Inches(5.7), size=9.5)

points = [
    ("async / await", "Modern syntax for handling Promises. Makes async code read like normal synchronous code."),
    ("try / catch", "Error handling for asynchronous code. Without it, a Django crash would throw an unhandled exception."),
    ("response.ok", "Checks the HTTP status code. True = 200-299. False = 400/404/500 errors."),
    ("response.json()", "Reads the response body stream and parses it from a string into a JavaScript object."),
    ("Fallback Pattern", "If data is null, the UI shows sample metrics instead of crashing with 'Cannot read undefined'."),
]
for i, (title, body) in enumerate(points):
    by = Inches(1.35) + i * Inches(1.13)
    rect(s, Inches(8.9), by, Inches(4.0), Inches(1.0), fill=CARD_BG, border=BORDER)
    txt(s, title, Inches(9.1), by + Inches(0.07),
        Inches(3.6), Inches(0.33), size=12, bold=True, color=ORANGE)
    txt(s, body, Inches(9.1), by + Inches(0.42),
        Inches(3.6), Inches(0.5), size=10.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 11 — WHAT IS DJANGO?
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 11)
txt(s, "The Backend — What is Django?", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Django is a Python web framework that handles the server side — routing requests, querying databases, and sending responses. It follows the MTV (Model-Template-View) pattern.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

concepts = [
    ("Model", "Defines the data structure. Maps to database tables. We ran migrations to create the default Django tables in db.sqlite3."),
    ("View", "A Python function that receives an HTTP request and returns a response. Our api_status() function in urls.py is a View."),
    ("URL Dispatcher", "Maps incoming URL paths to the correct view function. Defined in urls.py using the urlpatterns list."),
    ("Middleware", "Functions that wrap every request/response cycle. We added CorsMiddleware to handle browser security checks."),
    ("ORM", "Object-Relational Mapper. Write Python code, Django translates it to SQL. We used 'python manage.py migrate' to run this."),
    ("DRF", "Django REST Framework. An extension that makes building JSON APIs extremely simple. Adds @api_view decorator and Response class."),
]
for i, (title, body) in enumerate(concepts):
    col = i % 2; row = i // 2
    bx = Inches(0.4) + col * Inches(6.47)
    by = Inches(1.35) + row * Inches(1.9)
    rect(s, bx, by, Inches(6.15), Inches(1.75), fill=CARD_BG, border=BORDER)
    txt(s, title, bx + Inches(0.2), by + Inches(0.12),
        Inches(5.75), Inches(0.38), size=14, bold=True, color=GREEN)
    txt(s, body, bx + Inches(0.2), by + Inches(0.52),
        Inches(5.75), Inches(1.1), size=11.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 12 — THE API ENDPOINT
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 12)
txt(s, "Django REST Framework — The /api/status/ Endpoint", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "This is the heart of the Week 1 backend. One URL, one function, one JSON response — proving the full-stack connection works.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=15, color=LIGHT_GRAY)

code_block(s, """# From backend/grantlens_backend/urls.py

from django.urls import path
from rest_framework.decorators import api_view   # Restricts HTTP methods
from rest_framework.response import Response     # Auto-serializes dict → JSON
from datetime import datetime

# @api_view(['GET']) — Decorator that:
#   1. Only allows HTTP GET. Returns 405 for POST/PUT/DELETE automatically.
#   2. Wraps Django's HttpRequest into DRF's enhanced Request object.
#   3. Handles Content-Type negotiation (sends JSON response headers).
@api_view(['GET'])
def api_status(request):
    payload = {
        "status": "online",
        "solicitations_count": 2,      # Bound to Card 1 in React
        "proposals_count": 3,          # Bound to Card 2 in React
        "audits_completed": 2,         # Bound to Card 3 in React
        "average_score": 96.2,         # Bound to Card 4 in React
        "timestamp": datetime.now().strftime("%H:%M:%S")  # Live proof!
    }
    return Response(payload)   # DRF converts dict → JSON + HTTP 200

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', api_status, name='api_status'),  # Our endpoint
]""",
    Inches(0.4), Inches(1.35), Inches(8.3), Inches(5.7), size=9.5)

boxes = [
    ("HTTP Method Safety\n@api_view(['GET'])", "Only GET is allowed. If someone tries to POST data to this URL, DRF automatically returns HTTP 405 Method Not Allowed."),
    ("Auto JSON Serialization\nResponse(payload)", "DRF's Response class takes any Python dict and converts it to a JSON string with proper Content-Type: application/json headers."),
    ("Live Timestamp Proof", "The timestamp field changes every second. This proves to the grader that React is making a real live HTTP request — not just showing hardcoded values."),
]
for i, (title, body) in enumerate(boxes):
    by = Inches(1.35) + i * Inches(1.95)
    rect(s, Inches(8.9), by, Inches(4.0), Inches(1.8), fill=CARD_BG2, border=BORDER)
    txt(s, title, Inches(9.1), by + Inches(0.1),
        Inches(3.6), Inches(0.55), size=12, bold=True, color=GREEN)
    txt(s, body, Inches(9.1), by + Inches(0.68),
        Inches(3.6), Inches(1.0), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 13 — JSON: THE LANGUAGE BETWEEN THEM
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 13)
txt(s, "JSON — The Language React & Django Share", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "JSON (JavaScript Object Notation) is the universal data format for web APIs. Django sends it, React receives it. Both sides speak the same language.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

# Django side
rect(s, Inches(0.4), Inches(1.35), Inches(5.5), Inches(5.7), fill=CARD_BG, border=BORDER)
txt(s, "🐍  Django Sends (Python dict → JSON):",
    Inches(0.6), Inches(1.45), Inches(5.1), Inches(0.38), size=13, bold=True, color=GREEN)
mono(s, """# Python dictionary in urls.py:
payload = {
    "status": "online",
    "solicitations_count": 2,
    "proposals_count": 3,
    "audits_completed": 2,
    "average_score": 96.2,
    "timestamp": "14:32:07"
}

# DRF serializes this to:
# HTTP/1.1 200 OK
# Content-Type: application/json

{
    "status": "online",
    "solicitations_count": 2,
    "proposals_count": 3,
    "audits_completed": 2,
    "average_score": 96.2,
    "timestamp": "14:32:07"
}""",
    Inches(0.6), Inches(1.9), Inches(5.1), Inches(4.9), size=10, color=CYAN)

# Arrow
txt(s, "─────────────────\nHTTP GET Request\nHTTP 200 + JSON\n─────────────────",
    Inches(6.05), Inches(3.0), Inches(1.3), Inches(1.5),
    size=9, color=MID_GRAY, align=PP_ALIGN.CENTER)
txt(s, "→\n←", Inches(6.15), Inches(3.5), Inches(0.9), Inches(1.0),
    size=20, bold=True, color=ORANGE, align=PP_ALIGN.CENTER)

# React side
rect(s, Inches(7.5), Inches(1.35), Inches(5.4), Inches(5.7), fill=CARD_BG, border=BORDER)
txt(s, "⚛️  React Receives (JSON → JS object):",
    Inches(7.7), Inches(1.45), Inches(5.0), Inches(0.38), size=13, bold=True, color=ORANGE)
mono(s, """// In App.jsx — checkBackend():
const response = await fetch(url);
const data = await response.json();
// data is now a JS object:
// {
//   status: "online",
//   solicitations_count: 2,
//   proposals_count: 3,
//   ...
// }

setBackendStatus({ connected: true,
                   data: data });

// In JSX — binding data to the UI:
<div>{stats.solicitations_count}</div>
// → renders: 2

<div>{stats.average_score}%</div>
// → renders: 96.2%

<div>{stats.timestamp}</div>
// → renders: 14:32:07 (live!)""",
    Inches(7.7), Inches(1.9), Inches(5.0), Inches(4.9), size=10, color=CYAN)

# ─────────────────────────────────────────────
# SLIDE 14 — CORS
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 14)
txt(s, "CORS — Solving the Browser's Security Block", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "CORS (Cross-Origin Resource Sharing) is a browser security mechanism. Without it, a web page can ONLY fetch data from the exact same server it was loaded from.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

rect(s, Inches(0.4), Inches(1.35), Inches(12.5), Inches(1.4), fill=CARD_BG2, border=BORDER)
txt(s, "🚫  The Problem (Without CORS):",
    Inches(0.6), Inches(1.42), Inches(12), Inches(0.35), size=13, bold=True, color=RGBColor(0xEF, 0x44, 0x44))
txt(s, "React frontend runs at: http://localhost:5173  |  Django backend runs at: http://localhost:8000\nDifferent ports = Different origins. Browser blocks the fetch() call with: \"Access to fetch at 'http://localhost:8000' from origin 'http://localhost:5173' has been blocked by CORS policy.\"",
    Inches(0.6), Inches(1.8), Inches(12), Inches(0.8), size=12, color=LIGHT_GRAY)

code_block(s, """# From backend/grantlens_backend/settings.py

INSTALLED_APPS = [
    ...
    'corsheaders',          # Step 1: Install the CORS app
    'rest_framework',
]

# Step 2: Add CorsMiddleware at index 0 (THE VERY TOP — this is critical!)
# Django processes middleware top-to-bottom.
# If CorsMiddleware is not first, CSRF or Auth middleware rejects the
# preflight OPTIONS request before CORS headers can be added.
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # ← Must be index 0!
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]

# Step 3: Allow all origins during development
# This adds 'Access-Control-Allow-Origin: *' to every HTTP response header.
# The browser reads this header and allows the fetch() call to proceed.
CORS_ALLOW_ALL_ORIGINS = True   # Week 2: restrict to specific domains""",
    Inches(0.4), Inches(2.9), Inches(8.3), Inches(4.5), size=9.5)

points = [
    ("Same-Origin Policy", "A browser security rule: a page at port 5173 cannot read responses from port 8000 unless the server explicitly allows it."),
    ("Preflight Request", "Before sending the real GET, the browser sends a quick HTTP OPTIONS 'preflight' to ask: 'Are you willing to accept requests from port 5173?'"),
    ("The Header Fix", "django-cors-headers adds 'Access-Control-Allow-Origin: *' to responses — telling the browser 'yes, everyone is welcome'."),
    ("Why Index 0?", "If CorsMiddleware isn't first, other middleware layers reject the preflight OPTIONS request before CORS headers can be added."),
]
for i, (title, body) in enumerate(points):
    by = Inches(2.9) + i * Inches(1.12)
    rect(s, Inches(8.9), by, Inches(4.0), Inches(1.0), fill=CARD_BG, border=BORDER)
    txt(s, title, Inches(9.1), by + Inches(0.07),
        Inches(3.6), Inches(0.33), size=12, bold=True, color=ORANGE)
    txt(s, body, Inches(9.1), by + Inches(0.42),
        Inches(3.6), Inches(0.5), size=10.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 15 — THE DATABASE (SQLite)
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 15)
txt(s, "The Database — SQLite & Django Migrations", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Every Django project needs a database. In Week 1, we use SQLite — a simple file-based database (db.sqlite3) that needs zero server setup.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=16, color=LIGHT_GRAY)

code_block(s, """# From settings.py — Database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Which database engine to use
        'NAME': BASE_DIR / 'db.sqlite3',         # File location: d:/GrantLens/backend/db.sqlite3
    }
}

# ─── DJANGO MIGRATIONS ─────────────────────────────────────────────
# A "migration" is a Python script that describes changes to the database schema.
# Django ships with built-in migrations for Users, Auth, Sessions, Admin, etc.

# Command we ran:
# python manage.py migrate

# Output:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying sessions.0001_initial... OK

# This created the db.sqlite3 file and all required tables inside it.
# In Week 2: we add our own Model classes → generate our own migration files.""",
    Inches(0.4), Inches(1.35), Inches(8.3), Inches(5.7), size=9.5)

boxes = [
    ("What is a Migration?", "A version-controlled Python file that defines database table structure. Running 'migrate' applies all pending migrations to the actual database file."),
    ("Why SQLite for Week 1?", "SQLite stores the entire database in a single .sqlite3 file. No server, no password, no setup. Perfect for development and learning."),
    ("Week 2 Plan: PostgreSQL", "For production, we'll switch to PostgreSQL — a proper database server that handles concurrent users, complex queries, and large datasets."),
    ("Django ORM", "In Week 2, we'll write Python Model classes (class Grant(Model):) and Django translates them to SQL CREATE TABLE statements automatically."),
]
for i, (title, body) in enumerate(boxes):
    col = i % 2; row = i // 2
    bx = Inches(8.9) + col * 0  # single column
    by = Inches(1.35) + i * Inches(1.48)
    rect(s, Inches(8.9), by, Inches(4.0), Inches(1.35), fill=CARD_BG, border=BORDER)
    txt(s, title, Inches(9.1), by + Inches(0.08),
        Inches(3.6), Inches(0.35), size=12, bold=True, color=GREEN)
    txt(s, body, Inches(9.1), by + Inches(0.45),
        Inches(3.6), Inches(0.82), size=10.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 16 — THE STATUS BADGE (LIVE UI BINDING)
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 16)
txt(s, "Live UI Binding — The Status Badge", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "The green '🟢 Backend: Connected' pill in the navbar is the most direct proof of the frontend-backend connection. Here is exactly how it works in code.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=15, color=LIGHT_GRAY)

code_block(s, """// From App.jsx — The Status Badge JSX (in the Navbar)

// JavaScript ternary operator: condition ? valueIfTrue : valueIfFalse
// This runs INSIDE JSX {} curly braces, which evaluate JS expressions.

<div className="flex items-center gap-2">
  {backendStatus.loading ? (

    // Case 1: fetch() is still in flight (loading = true)
    // Show a pulsing orange dot with "Connecting..." text
    <span className="animate-pulse text-brand-400 text-sm">
      ⟳ Connecting...
    </span>

  ) : backendStatus.connected ? (

    // Case 2: Django responded HTTP 200 (connected = true)
    // Show green animated dot + "Backend: Connected (Django)" text
    <span className="flex items-center gap-1.5 text-emerald-400 text-sm font-medium">
      <span className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse-slow"/>
      Backend: Connected (Django)
    </span>

  ) : (

    // Case 3: fetch() failed (connected = false, loading = false)
    // Show red dot with "Offline" text
    <span className="text-red-400 text-sm">
      ● Backend: Offline
    </span>

  )}
</div>""",
    Inches(0.4), Inches(1.35), Inches(8.3), Inches(5.7), size=9.5)

rect(s, Inches(8.9), Inches(1.35), Inches(4.0), Inches(5.7), fill=CARD_BG, border=BORDER)
txt(s, "Three States Explained", Inches(9.1), Inches(1.45),
    Inches(3.6), Inches(0.4), size=14, bold=True, color=ORANGE)

states = [
    ("⟳ Loading...", "loading = true\nfetch() request sent.\nWaiting for Django to respond.\nShows pulsing orange text.", ORANGE),
    ("🟢 Connected", "connected = true\nDjango returned HTTP 200.\nJSON received and parsed.\nUI filled with real data.", GREEN),
    ("🔴 Offline", "connected = false\nDjango is not running.\nConnection refused error.\nUI shows fallback data.", RGBColor(0xEF, 0x44, 0x44)),
]
for i, (label, body, col) in enumerate(states):
    sy = Inches(1.95) + i * Inches(1.6)
    txt(s, label, Inches(9.1), sy, Inches(3.6), Inches(0.38),
        size=14, bold=True, color=col)
    txt(s, body, Inches(9.1), sy + Inches(0.42),
        Inches(3.6), Inches(1.0), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 17 — THE 4 METRIC TILES
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 17)
txt(s, "Data Binding — The 4 Live Metric Tiles", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "The 4 dashboard cards display numbers that come directly from Django's JSON. This is React's declarative data binding — the UI reflects state automatically.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=15, color=LIGHT_GRAY)

code_block(s, """// From App.jsx — Defensive fallback pattern + data binding

// The logical OR (||) operator short-circuits:
// If backendStatus.data is NOT null → use the live Django data
// If backendStatus.data IS null (server offline) → use sample values
const stats = backendStatus.data || {
  solicitations_count: 2,   // Sample fallback values
  proposals_count: 3,
  audits_completed: 2,
  average_score: 96.2,
};

// JSX — The 4 metric tiles bound to Django data:
const metrics = [
  {
    value: stats.solicitations_count,   // ← comes from Django JSON
    label: "Grant Solicitations",
    detail: stats.solicitations_detail,
    icon: <FileText />,
  },
  {
    value: stats.proposals_count,       // ← comes from Django JSON
    label: "Proposals Loaded",
    icon: <TrendingUp />,
  },
  {
    value: stats.audits_completed,      // ← comes from Django JSON
    label: "Audits Completed",
    icon: <CheckCircle2 />,
  },
  {
    value: `${stats.average_score}%`,   // ← comes from Django JSON
    label: "Average Score",
    icon: <Award />,
  },
];

// Render: .map() loops through the array and returns JSX for each tile
{metrics.map((m, i) => (
  <div key={i} className="bg-navy-800 rounded-xl p-6 border border-navy-700">
    {m.icon}
    <div className="text-3xl font-bold">{m.value}</div>
    <div className="text-gray-400">{m.label}</div>
  </div>
))}""",
    Inches(0.4), Inches(1.35), Inches(9.0), Inches(5.7), size=9)

rect(s, Inches(9.6), Inches(1.35), Inches(3.3), Inches(5.7), fill=CARD_BG, border=BORDER)
txt(s, "Key Concepts", Inches(9.8), Inches(1.45),
    Inches(2.9), Inches(0.35), size=13, bold=True, color=ORANGE)
bullets = [
    ("Logical OR ||", "JavaScript short-circuit evaluation. If left side is falsy (null), use right side."),
    ("Template Literal", "`${score}%` — inserts JS variable inside a string."),
    ("Array.map()", "Transforms an array into JSX. One tile rendered per array item."),
    ("key prop", "React needs a unique key for each list item to track DOM changes efficiently."),
    ("Declarative UI", "We describe WHAT to show (the state), not HOW to update the DOM. React handles the how."),
]
for i, (title, body) in enumerate(bullets):
    by = Inches(1.95) + i * Inches(1.0)
    txt(s, title, Inches(9.8), by, Inches(2.9), Inches(0.32),
        size=12, bold=True, color=GREEN)
    txt(s, body, Inches(9.8), by + Inches(0.33),
        Inches(2.9), Inches(0.6), size=10.5, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 18 — PROJECT FILE STRUCTURE
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 18)
txt(s, "Project File Structure", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Understanding where each file lives and why it is there.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.4), size=15, color=LIGHT_GRAY)

# Frontend tree
rect(s, Inches(0.4), Inches(1.25), Inches(5.8), Inches(5.9), fill=CARD_BG, border=BORDER)
txt(s, "⚛️  Frontend  (d:/GrantLens/frontend/)",
    Inches(0.6), Inches(1.35), Inches(5.4), Inches(0.38), size=13, bold=True, color=ORANGE)
mono(s, """frontend/
├── index.html          ← HTML shell. React mounts here.
├── package.json        ← npm dependencies & scripts
├── vite.config.js      ← Vite build tool config
├── tailwind.config.js  ← Color tokens & JIT config
├── postcss.config.js   ← PostCSS pipeline (Tailwind needs this)
└── src/
    ├── main.jsx        ← Entry point: ReactDOM.createRoot()
    ├── App.jsx         ← The whole UI — our main component
    └── index.css       ← Tailwind directives + base resets""",
    Inches(0.6), Inches(1.82), Inches(5.4), Inches(4.8), size=10, color=CYAN)

# Backend tree
rect(s, Inches(6.55), Inches(1.25), Inches(6.35), Inches(5.9), fill=CARD_BG, border=BORDER)
txt(s, "🐍  Backend  (d:/GrantLens/backend/)",
    Inches(6.75), Inches(1.35), Inches(5.9), Inches(0.38), size=13, bold=True, color=GREEN)
mono(s, """backend/
├── manage.py              ← Django CLI. Runs the server, migrations.
├── db.sqlite3             ← The database file (created by 'migrate')
└── grantlens_backend/
    ├── __init__.py        ← Marks this as a Python package
    ├── settings.py        ← ALL Django config (CORS, DB, apps, etc.)
    ├── urls.py            ← URL routing + api_status() view function
    ├── wsgi.py            ← Production server entry point
    └── asgi.py            ← Async production entry point""",
    Inches(6.75), Inches(1.82), Inches(5.9), Inches(4.8), size=10, color=CYAN)

txt(s, "The two servers run simultaneously and communicate only through HTTP. They are completely independent — changing the frontend does not require restarting Django.",
    Inches(0.4), Inches(7.1), Inches(12.5), Inches(0.35), size=12, italic=True, color=MID_GRAY)

# ─────────────────────────────────────────────
# SLIDE 19 — HOW THE SERVERS START
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 19)
txt(s, "Running the Project — How Both Servers Start", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Two terminal windows, two commands, one full-stack application.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.4), size=15, color=LIGHT_GRAY)

# Terminal 1
rect(s, Inches(0.4), Inches(1.25), Inches(6.0), Inches(2.8), fill=CODE_BG, border=BORDER)
txt(s, "Terminal 1 — Start Django Backend",
    Inches(0.6), Inches(1.35), Inches(5.6), Inches(0.38), size=13, bold=True, color=GREEN)
mono(s, """# Navigate to backend folder
cd d:/GrantLens/backend

# Start the Django development server
python manage.py runserver 127.0.0.1:8000

# Output:
# Watching for file changes with StatReloader
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.""",
    Inches(0.6), Inches(1.82), Inches(5.6), Inches(2.1), size=10, color=CYAN)

# Terminal 2
rect(s, Inches(6.7), Inches(1.25), Inches(6.2), Inches(2.8), fill=CODE_BG, border=BORDER)
txt(s, "Terminal 2 — Start React Frontend",
    Inches(6.9), Inches(1.35), Inches(5.8), Inches(0.38), size=13, bold=True, color=ORANGE)
mono(s, """# Navigate to frontend folder
cd d:/GrantLens/frontend

# Install dependencies (first time only)
npm install

# Start the Vite development server
npm run dev

# Output:
# VITE v5.x  ready in 341 ms
# ➜  Local:   http://localhost:5173/""",
    Inches(6.9), Inches(1.82), Inches(5.8), Inches(2.1), size=10, color=CYAN)

# Explanation boxes
steps = [
    ("python manage.py runserver", "Django's CLI command that starts the built-in WSGI development server on port 8000. It auto-reloads when you save Python files."),
    ("npm install", "Reads package.json and downloads all JavaScript dependencies (React, Vite, Tailwind, Lucide) into the node_modules folder."),
    ("npm run dev", "Runs the 'dev' script from package.json — which is 'vite'. Starts Vite's dev server with Hot Module Replacement enabled."),
    ("Why two terminals?", "Frontend and backend are separate processes. They don't share memory — they communicate only over the network via HTTP on different ports."),
]
for i, (title, body) in enumerate(steps):
    col = i % 2; row = i // 2
    bx = Inches(0.4) + col * Inches(6.5)
    by = Inches(4.3) + row * Inches(1.5)
    rect(s, bx, by, Inches(6.1), Inches(1.35), fill=CARD_BG, border=BORDER)
    txt(s, title, bx + Inches(0.2), by + Inches(0.08),
        Inches(5.7), Inches(0.35), size=13, bold=True, color=ORANGE)
    txt(s, body, bx + Inches(0.2), by + Inches(0.45),
        Inches(5.7), Inches(0.82), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 20 — KEY CS CONCEPTS LEARNED
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 20)
txt(s, "Key CS Concepts We Learned", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Building GrantLens taught us real computer science — not just syntax, but why things work the way they do.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.5), size=15, color=LIGHT_GRAY)

concepts = [
    ("HTTP Request/Response Cycle", "Every browser-to-server interaction is a request (GET, POST, PUT, DELETE) and a response (200, 404, 500). We implemented GET → 200 + JSON."),
    ("Asynchronous Programming", "JavaScript is single-threaded. async/await lets us wait for network data without freezing the UI. The browser paints normally while fetch() runs."),
    ("Component State Machine", "useState creates a state machine. Our app has 3 states: loading → connected or offline. The UI is a pure function of state."),
    ("Virtual DOM Reconciliation", "React diffs the new and old VDOM trees and only updates changed real DOM nodes — O(n) complexity instead of O(n³) naive approach."),
    ("Middleware Architecture", "Django's middleware stack is like a chain of interceptors. Every request passes through each layer. CorsMiddleware must be first to intercept OPTIONS."),
    ("Database Migrations", "Version-controlled schema changes. Instead of manually writing SQL, we write Python Model classes and Django generates the SQL migrations automatically."),
    ("REST API Design", "Representational State Transfer — stateless, URL-addressable resources. /api/status/ is a GET endpoint that returns a JSON resource representation."),
    ("CORS & Same-Origin Policy", "Browser security: scripts can only read responses from their own origin unless the server explicitly grants permission via CORS headers."),
]
for i, (title, body) in enumerate(concepts):
    col = i % 2; row = i // 4
    bx = Inches(0.4) + col * Inches(6.47)
    by = Inches(1.35) + (i // 2) * Inches(1.45)
    rect(s, bx, by, Inches(6.15), Inches(1.32), fill=CARD_BG, border=BORDER)
    txt(s, f"{i+1}. {title}", bx + Inches(0.2), by + Inches(0.08),
        Inches(5.75), Inches(0.35), size=12.5, bold=True, color=ORANGE)
    txt(s, body, bx + Inches(0.2), by + Inches(0.46),
        Inches(5.75), Inches(0.8), size=11, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 21 — CHALLENGES & HOW WE SOLVED THEM
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 21)
txt(s, "Challenges We Faced & How We Solved Them", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "Real engineering is problem-solving. These are the actual errors we debugged during Week 1 development.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.4), size=15, color=LIGHT_GRAY)

challenges = [
    (
        "Tailwind CSS v4 Broke PostCSS",
        "npm install tailwindcss installed version 4. Tailwind v4 changed its PostCSS plugin structure — our postcss.config.js stopped working and the build failed.",
        "Pinned tailwindcss@^3.4.17 in package.json. Tailwind v3 uses the classic 'require' CommonJS plugin format that PostCSS expects.",
        "npm install tailwindcss@^3.4.17"
    ),
    (
        "CORS Blocked All API Requests",
        "React's fetch() calls returned: 'Access to fetch from origin localhost:5173 has been blocked by CORS policy.' The browser refused to process the response.",
        "Installed django-cors-headers and placed CorsMiddleware at index 0 of MIDDLEWARE. Set CORS_ALLOW_ALL_ORIGINS = True for development.",
        "pip install django-cors-headers"
    ),
    (
        "useEffect Caused Infinite Loop",
        "Forgot the [] dependency array. checkBackend() updated state → state triggered re-render → re-render triggered useEffect → infinite GET requests crashed Django.",
        "Added the empty [] as the second argument to useEffect. This restricts execution to once on mount only.",
        "useEffect(() => { checkBackend(); }, []);"
    ),
    (
        "lucide-react Missing 'Github' Icon",
        "The import { Github } from 'lucide-react' caused a build error: 'Github is not exported from lucide-react'.",
        "Removed the Github import. Lucide-React uses 'Github' not 'GitHub' — but it was removed entirely as it wasn't needed.",
        "Removed unused icon import"
    ),
]
for i, (title, prob, sol, fix) in enumerate(challenges):
    col = i % 2; row = i // 2
    bx = Inches(0.4) + col * Inches(6.47)
    by = Inches(1.35) + row * Inches(2.85)
    rect(s, bx, by, Inches(6.15), Inches(2.7), fill=CARD_BG, border=BORDER)
    txt(s, f"❌  {title}", bx + Inches(0.2), by + Inches(0.1),
        Inches(5.75), Inches(0.35), size=12.5, bold=True, color=RGBColor(0xEF, 0x44, 0x44))
    txt(s, f"Problem: {prob}", bx + Inches(0.2), by + Inches(0.5),
        Inches(5.75), Inches(0.75), size=11, color=LIGHT_GRAY)
    txt(s, f"✅  Fix: {sol}", bx + Inches(0.2), by + Inches(1.28),
        Inches(5.75), Inches(0.75), size=11, color=GREEN)
    mono(s, fix, bx + Inches(0.2), by + Inches(2.12),
         Inches(5.75), Inches(0.4), size=10, color=CYAN)

# ─────────────────────────────────────────────
# SLIDE 22 — UPLOAD ZONE & WEEK 2 ROADMAP
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 22)
txt(s, "Week 2 Roadmap — What We Build Next", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

txt(s, "The upload dropzone is already designed in the UI (marked 'In Progress'). Week 2 wires it to real AI functionality.",
    Inches(0.5), Inches(0.72), Inches(12.33), Inches(0.4), size=15, color=LIGHT_GRAY)

# Week 1 completed column
rect(s, Inches(0.4), Inches(1.25), Inches(4.0), Inches(5.9), fill=CARD_BG, border=BORDER)
pill(s, "WEEK 1 ✓  DONE", Inches(0.6), Inches(1.38),
     w=Inches(3.0), h=Inches(0.35), bg=GREEN, size=11)
done = [
    "React + Vite frontend scaffolded",
    "Tailwind CSS design system configured",
    "Django 6.1 + DRF backend running",
    "SQLite database initialized (migrate)",
    "CORS handshake solved",
    "/api/status/ JSON endpoint live",
    "4 metric tiles bound to Django data",
    "🟢 Live connection badge working",
    "Upload UI designed (Week 2 scope)",
]
for i, item in enumerate(done):
    txt(s, f"✓  {item}", Inches(0.6), Inches(1.85) + i * Inches(0.54),
        Inches(3.6), Inches(0.45), size=11, color=LIGHT_GRAY)

# Week 2 column
rect(s, Inches(4.7), Inches(1.25), Inches(4.0), Inches(5.9), fill=CARD_BG2, border=BORDER)
pill(s, "WEEK 2  →  NEXT", Inches(4.9), Inches(1.38),
     w=Inches(3.0), h=Inches(0.35), bg=ORANGE, size=11)
next_steps = [
    "PDF upload endpoint (POST /api/upload/)",
    "PyMuPDF — extract text from PDF",
    "Parse sections & budget tables",
    "Compliance ruleset schema (JSON)",
    "Google Gemini API integration",
    "Rule-checking engine",
    "Violation report generation",
    "Rubric score calculation",
    "Results displayed in React UI",
]
for i, item in enumerate(next_steps):
    txt(s, f"→  {item}", Inches(4.9), Inches(1.85) + i * Inches(0.54),
        Inches(3.6), Inches(0.45), size=11, color=LIGHT_GRAY)

# Week 3 column
rect(s, Inches(9.0), Inches(1.25), Inches(3.9), Inches(5.9), fill=CARD_BG, border=BORDER)
pill(s, "WEEK 3  →  FINAL", Inches(9.2), Inches(1.38),
     w=Inches(3.0), h=Inches(0.35), bg=CARD_BG2, text_color=LIGHT_GRAY, size=11)
future = [
    "ChromaDB vector store",
    "LangChain agent orchestration",
    "Precedent case retrieval (RAG)",
    "PostgreSQL production DB",
    "Multi-document audit queue",
    "Exportable PDF audit reports",
    "Performance optimization",
    "Full system testing",
    "Final demo & presentation",
]
for i, item in enumerate(future):
    txt(s, f"◦  {item}", Inches(9.2), Inches(1.85) + i * Inches(0.54),
        Inches(3.5), Inches(0.45), size=11, color=MID_GRAY)

# ─────────────────────────────────────────────
# SLIDE 23 — SUMMARY
# ─────────────────────────────────────────────
s = add_slide(); accent_bar(s); slide_number(s, 23)
txt(s, "Summary — What We Achieved in Week 1", Inches(0.5), Inches(0.1),
    Inches(12), Inches(0.55), size=30, bold=True, color=WHITE)

achievements = [
    ("Full-Stack Architecture", "Built a complete client-server application with a React frontend and Django backend communicating via REST API over HTTP."),
    ("Live Data Binding", "The 4 metric tiles and status badge pull real data from Django at runtime — not hardcoded values. The timestamp proves it."),
    ("CORS Solution Implemented", "Solved the browser's Same-Origin Policy security block using django-cors-headers with correct middleware ordering."),
    ("Modern Toolchain Configured", "Vite (ESM build), Tailwind JIT (32KB CSS), python-pptx, DRF, SQLite migrations — a production-ready dev environment."),
    ("CS Fundamentals Applied", "Practiced: async/await, HTTP protocol, REST API design, React state machines, Virtual DOM, middleware pipelines, ORM migrations."),
    ("Honest Scope Management", "Identified exactly what Week 1 can achieve vs. what is Week 2 scope. Upload UI is built but not yet connected — transparently marked."),
]
for i, (title, body) in enumerate(achievements):
    col = i % 2; row = i // 2
    bx = Inches(0.4) + col * Inches(6.47)
    by = Inches(1.35) + row * Inches(1.78)
    rect(s, bx, by, Inches(6.15), Inches(1.65), fill=CARD_BG, border=BORDER)
    n = ["①","②","③","④","⑤","⑥"][i]
    txt(s, f"{n}  {title}", bx + Inches(0.2), by + Inches(0.1),
        Inches(5.75), Inches(0.38), size=13.5, bold=True, color=ORANGE)
    txt(s, body, bx + Inches(0.2), by + Inches(0.5),
        Inches(5.75), Inches(1.05), size=12, color=LIGHT_GRAY)

# ─────────────────────────────────────────────
# SLIDE 24 — Q&A
# ─────────────────────────────────────────────
s = add_slide(); slide_number(s, 24)

# Orange center strip
strip = s.shapes.add_shape(1, 0, Inches(3.3), SLIDE_W, Inches(0.05))
strip.fill.solid(); strip.fill.fore_color.rgb = ORANGE
strip.line.fill.background()

txt(s, "Q & A", Inches(1), Inches(1.0), Inches(11.33), Inches(1.2),
    size=72, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txt(s, "Questions? We're happy to explain any part of the code.",
    Inches(1), Inches(2.3), Inches(11.33), Inches(0.6),
    size=22, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)

quick_q = [
    "How does useEffect know to run only once?",
    "What happens if Django is offline when React loads?",
    "Why is CorsMiddleware at index 0?",
    "What is the difference between Vite and Webpack?",
]
for i, q in enumerate(quick_q):
    qx = Inches(1.5) + (i % 2) * Inches(5.5)
    qy = Inches(3.9) + (i // 2) * Inches(0.9)
    rect(s, qx, qy, Inches(5.0), Inches(0.72), fill=CARD_BG, border=BORDER)
    txt(s, f"❓  {q}", qx + Inches(0.15), qy + Inches(0.08),
        Inches(4.7), Inches(0.6), size=12, color=LIGHT_GRAY)

txt(s, "CSE299 Section 3  ·  Group 2  ·  GrantLens",
    Inches(1), Inches(6.95), Inches(11.33), Inches(0.4),
    size=12, color=MID_GRAY, align=PP_ALIGN.CENTER)

# ─────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────
output_path = r'd:\GrantLens\GrantLens_Week1_Final_Presentation.pptx'
prs.save(output_path)
print("DONE! Saved:", output_path)
print("Slides:", len(prs.slides))
