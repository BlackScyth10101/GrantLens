export const CORE_FEATURES = [
  {
    id: "ingestion",
    iconName: "FileText",
    tag: "Dual-Engine Parsing",
    badgeColor: "cyan",
    title: "Document Ingestion Engine",
    description: "High-precision PDF & DOCX ingestion utilizing PyMuPDF (fitz) for typographic geometry, bounding boxes, and heading trees alongside pdfplumber for multi-column financial tables.",
    metrics: "Sub-second 50-page layout extraction",
    technicalStack: "PyMuPDF • pdfplumber • LayoutLM",
  },
  {
    id: "rule-extraction",
    iconName: "ShieldAlert",
    tag: "Automated Constraint Mining",
    badgeColor: "amber",
    title: "Rulebook Constraint Extraction",
    description: "Converts dense, 200-page federal solicitation manuals into structured, machine-verifiable compliance graphs. Enforces mandatory headings, font sizes, margins, and page caps.",
    metrics: "Supports NSF PAPPG 24-1, NIH SF424, DOE, DARPA",
    technicalStack: "Regex Rulesets • LLM Constraint Parsing",
  },
  {
    id: "budget-reconciliation",
    iconName: "Calculator",
    tag: "Financial Integrity",
    badgeColor: "emerald",
    title: "Budget-to-Narrative Reconciliation",
    description: "Cross-checks tabular financial sheets against descriptive narrative prose. Identifies mismatches in person-months, fringe rates, subawards, and equipment thresholds down to the penny.",
    metrics: "Detects hidden discrepancies across 100+ line items",
    technicalStack: "Table Parsing • Fuzzy Matcher • Exact Math Audit",
  },
  {
    id: "rubric-scoring",
    iconName: "Award",
    tag: "Calibrated 0–100 Rubric",
    badgeColor: "purple",
    title: "0–100 Rubric Scoring Engine",
    description: "Simulates an official federal review panel assessment. Computes a quantitative compliance fidelity score broken down across Intellectual Merit, Broader Impacts, and Technical Feasibility.",
    metrics: "Calibrated to federal panel scoring distributions",
    technicalStack: "Weighted Criteria • Recharts Visualizer",
  },
  {
    id: "targeted-rewrites",
    iconName: "Wand2",
    tag: "Context-Preserving Rewrites",
    badgeColor: "orange",
    title: "Targeted Rewrite Generator",
    description: "Produces non-hallucinatory, targeted prose edits for flagged sections. Condenses overlength project descriptions, repairs ambiguous Broader Impacts, and preserves citations.",
    metrics: "Cuts up to 15% text volume with 0% citation loss",
    technicalStack: "Google Gemini 1.5 Pro • Strict Token Budgeting",
  },
  {
    id: "grounded-rag",
    iconName: "Compass",
    tag: "Strict Citation Grounding",
    badgeColor: "blue",
    title: "Grounded RAG Guideline Q&A",
    description: "Ask natural language questions regarding allowable expenses, foreign component disclosure, or data management policies with direct section and page number citations.",
    metrics: "100% cited answers against ChromaDB vector store",
    technicalStack: "ChromaDB • LangChain • Gemini Flash",
  },
];

export const WORKFLOW_STEPS = [
  {
    step: "01",
    title: "Upload Solicitation & Proposal Draft",
    subtitle: "RFP Rulebook + Proposal Package",
    description: "Drop your official federal solicitation PDF (NSF, NIH, DOE) and your draft proposal files (PDF or DOCX). Our parser builds the semantic heading tree and extracts all tabular budgets in seconds.",
    bullets: ["Automatic layout & font detection", "Deep tabular parsing for multi-page budgets", "Confidential local sandbox processing"],
    badge: "PyMuPDF & pdfplumber",
  },
  {
    step: "02",
    title: "AI Audits, Reconciles & Evaluates",
    subtitle: "Triple-Engine Compliance Validation",
    description: "GrantLens matches your document against mandatory rules. It runs numerical budget cross-reconciliation, flags missing sections or page cap spills, and runs multi-dimensional rubric scoring.",
    bullets: ["Fatal error detection (desk-reject prevention)", "Narrative-to-budget financial reconciliation", "0–100 calibrated panel score estimation"],
    badge: "LangChain + Gemini + Rules Engine",
  },
  {
    step: "03",
    title: "Export Verified Compliance Dossier",
    subtitle: "Pre-Submission Audit Report",
    description: "Review color-coded red/yellow/green findings with actionable rewrite suggestions. Export an executive summary PDF to share with co-PIs and your University Sponsored Research Office.",
    bullets: ["Side-by-side targeted text rewrite diffs", "Exportable audit certification report", "Zero hallucination guarantee with exact rule citations"],
    badge: "Ready for Research.gov / Grants.gov",
  },
];

export const COMPARISON_DATA = {
  manual: [
    { label: "Time Investment", text: "40+ hours spent manually flipping through 180-page PAPPG rulebooks." },
    { label: "Budget Checks", text: "Silent discrepancies between Table 2 numbers and Section 6 prose slip through." },
    { label: "Rejection Risk", text: "30% administrative desk-rejections occur before peer review ever reads the science." },
    { label: "Review Calibration", text: "Subjective guesswork on whether Broader Impacts meets agency priority criteria." },
    { label: "Guideline Clarity", text: "Hours wasted trying to interpret ambiguous subaward and collaborator rules." }
  ],
  automated: [
    { label: "Time Investment", text: "30-second automated scan covering 100% of formatting and layout constraints." },
    { label: "Budget Checks", text: "Automated tabular vs. narrative cross-reconciliation down to the dollar and month." },
    { label: "Rejection Risk", text: "Fatal error gatekeeper catches overlength sections and missing headings instantly." },
    { label: "Review Calibration", text: "Simulated 0–100 federal rubric score with dimension-specific breakdown." },
    { label: "Guideline Clarity", text: "RAG Q&A grounded in official solicitation rulebooks with exact page citations." }
  ]
};
