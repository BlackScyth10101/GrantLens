import React, { useState } from 'react';
import { 
  Upload, 
  FileText, 
  CheckCircle2, 
  AlertTriangle, 
  XCircle, 
  ShieldAlert, 
  DollarSign, 
  Award, 
  ArrowRight, 
  RotateCcw,
  Sparkles,
  FileCheck,
  Building
} from 'lucide-react';

export default function SubmissionPortal({ user, token, onSignOut }) {
  const [title, setTitle] = useState('');
  const [fundingAgency, setFundingAgency] = useState('NSF 24-500 (National Science Foundation)');
  const [solicitationFile, setSolicitationFile] = useState(null);
  const [proposalFile, setProposalFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [auditResult, setAuditResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!solicitationFile || !proposalFile) {
      setError('Please provide both the Solicitation (Call) PDF and your Draft Proposal PDF.');
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('title', title);
    formData.append('funding_agency', fundingAgency);
    formData.append('solicitation_file', solicitationFile);
    formData.append('proposal_file', proposalFile);

    try {
      const response = await fetch('http://localhost:8000/api/v1/submissions/upload', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        },
        body: formData,
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || 'Audit processing failed on backend.');
      }

      setAuditResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setAuditResult(null);
    setSolicitationFile(null);
    setProposalFile(null);
    setTitle('');
  };

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Researcher header info bar */}
      <div className="bg-navy-900 border border-navy-800 rounded-2xl p-5 mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div className="flex items-center gap-3.5">
          <div className="w-11 h-11 rounded-xl bg-brand-500/10 border border-brand-500/20 flex items-center justify-center text-brand-400 font-bold text-lg">
            {user?.full_name ? user.full_name[0] : 'R'}
          </div>
          <div>
            <h2 className="text-white font-semibold text-base">{user?.full_name || 'Authenticated Researcher'}</h2>
            <p className="text-xs text-slate-400 flex items-center gap-1.5">
              <span>{user?.institution || 'Academic Institution'}</span>
              <span>•</span>
              <span className="text-brand-400">{user?.department || 'Research Faculty'}</span>
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <span className="text-xs bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 px-3 py-1.5 rounded-full font-medium flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            FastAPI Audit Pipeline Active
          </span>
          <button
            onClick={onSignOut}
            className="text-xs bg-navy-800 hover:bg-navy-750 text-slate-300 px-3 py-1.5 rounded-lg border border-navy-700 transition-colors"
          >
            Sign Out
          </button>
        </div>
      </div>

      {!auditResult ? (
        /* Upload Form */
        <div className="bg-navy-900 border border-navy-800 rounded-2xl p-8 backdrop-blur-xl">
          <div className="max-w-2xl mb-8">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-500/10 border border-brand-500/20 text-brand-400 text-xs font-semibold uppercase tracking-wider mb-3">
              <Sparkles className="w-3.5 h-3.5" />
              Dual-Document Ingestion Engine
            </div>
            <h1 className="text-2xl font-bold text-white tracking-tight">Pre-Flight Grant Audit Submission</h1>
            <p className="text-sm text-slate-400 mt-1">
              Upload the agency solicitation PDF and your proposal manuscript. GrantLens evaluates page limits, font geometry, budget line-items, and mandatory sections.
            </p>
          </div>

          {error && (
            <div className="mb-6 p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-xs text-red-300 flex items-start gap-2.5">
              <XCircle className="w-4 h-4 text-red-400 shrink-0 mt-0.5" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">Proposal Working Title</label>
                <input
                  type="text"
                  required
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  placeholder="e.g. Scalable Quantum Error Correction in Diamond NV Centers"
                  className="w-full bg-navy-950 border border-navy-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-1.5">Target Funding Agency / Solicitation Call</label>
                <select
                  value={fundingAgency}
                  onChange={(e) => setFundingAgency(e.target.value)}
                  className="w-full bg-navy-950 border border-navy-800 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-brand-500 transition-colors"
                >
                  <option value="NSF 24-500 (National Science Foundation)">NSF 24-500 (National Science Foundation)</option>
                  <option value="NIH R01 Research Project Grant">NIH R01 Research Project Grant</option>
                  <option value="DOE Early Career Research Program">DOE Early Career Research Program</option>
                  <option value="Horizon Europe Pillar II">Horizon Europe Pillar II</option>
                  <option value="Custom Agency Solicitation">Custom Agency Solicitation</option>
                </select>
              </div>
            </div>

            {/* Dual File Dropzones */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
              {/* Solicitation File */}
              <div className="border-2 border-dashed border-navy-750 hover:border-brand-500/50 rounded-2xl p-6 text-center transition-colors bg-navy-950/50">
                <FileText className="w-10 h-10 text-cyan-400 mx-auto mb-3" />
                <h3 className="text-sm font-semibold text-white mb-1">Agency Call / Solicitation PDF</h3>
                <p className="text-xs text-slate-400 mb-4">Ingests guidelines, format rules, budget caps</p>
                
                <input
                  type="file"
                  id="solicitationInput"
                  accept=".pdf,application/pdf"
                  onChange={(e) => setSolicitationFile(e.target.files[0])}
                  className="hidden"
                />
                <label
                  htmlFor="solicitationInput"
                  className="inline-flex items-center gap-2 px-4 py-2 bg-navy-800 hover:bg-navy-700 text-xs font-semibold text-slate-200 rounded-lg cursor-pointer transition-colors"
                >
                  <Upload className="w-3.5 h-3.5" />
                  {solicitationFile ? solicitationFile.name : 'Select Solicitation PDF'}
                </label>
              </div>

              {/* Proposal File */}
              <div className="border-2 border-dashed border-navy-750 hover:border-brand-500/50 rounded-2xl p-6 text-center transition-colors bg-navy-950/50">
                <FileCheck className="w-10 h-10 text-brand-400 mx-auto mb-3" />
                <h3 className="text-sm font-semibold text-white mb-1">Draft Proposal Manuscript PDF</h3>
                <p className="text-xs text-slate-400 mb-4">Ingests narrative, layout geometry, tables, and budget sheet</p>
                
                <input
                  type="file"
                  id="proposalInput"
                  accept=".pdf,application/pdf"
                  onChange={(e) => setProposalFile(e.target.files[0])}
                  className="hidden"
                />
                <label
                  htmlFor="proposalInput"
                  className="inline-flex items-center gap-2 px-4 py-2 bg-brand-500 hover:bg-brand-400 text-xs font-semibold text-slate-950 rounded-lg cursor-pointer transition-colors"
                >
                  <Upload className="w-3.5 h-3.5" />
                  {proposalFile ? proposalFile.name : 'Select Proposal PDF'}
                </label>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-3.5 px-6 rounded-xl bg-brand-500 hover:bg-brand-400 text-slate-950 font-bold text-sm flex items-center justify-center gap-2 shadow-xl shadow-brand-500/20 disabled:opacity-50 transition-all cursor-pointer"
            >
              {loading ? (
                <span>Extracting Geometry & Tables with PyMuPDF & pdfplumber...</span>
              ) : (
                <>
                  <span>Execute Automated Pre-Flight Compliance Audit</span>
                  <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>
          </form>
        </div>
      ) : (
        /* Results View */
        <div className="space-y-6">
          {/* Top banner card */}
          <div className="bg-navy-900 border border-navy-800 rounded-2xl p-6 backdrop-blur-xl">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-navy-800">
              <div>
                <span className="text-xs font-bold text-brand-400 uppercase tracking-wider">Audit Evaluation Complete</span>
                <h2 className="text-2xl font-bold text-white mt-1">{auditResult.title}</h2>
                <p className="text-xs text-slate-400 mt-1">Agency Target: {auditResult.funding_agency}</p>
              </div>

              <div className="flex items-center gap-4">
                <div className="text-right">
                  <span className="text-xs text-slate-400 block">Compliance Score</span>
                  <span className={`text-3xl font-extrabold ${auditResult.audit_score >= 80 ? 'text-emerald-400' : 'text-amber-400'}`}>
                    {auditResult.audit_score.toFixed(1)}%
                  </span>
                </div>
                <div className={`px-4 py-2 rounded-xl text-xs font-bold border ${
                  auditResult.institutional_signoff_ready 
                    ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400'
                    : 'bg-red-500/10 border-red-500/30 text-red-400'
                }`}>
                  {auditResult.institutional_signoff_ready ? '✓ SRO Clearance Ready' : '⚠ Action Required'}
                </div>
              </div>
            </div>

            {/* Quick metrics grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
              <div className="bg-navy-950/60 p-4 rounded-xl border border-navy-800/80">
                <span className="text-xs text-slate-400 block mb-1">Solicitation Pages</span>
                <span className="text-xl font-bold text-white">{auditResult.solicitation_pages}</span>
              </div>
              <div className="bg-navy-950/60 p-4 rounded-xl border border-navy-800/80">
                <span className="text-xs text-slate-400 block mb-1">Proposal Pages</span>
                <span className="text-xl font-bold text-white">{auditResult.proposal_pages}</span>
              </div>
              <div className="bg-navy-950/60 p-4 rounded-xl border border-navy-800/80">
                <span className="text-xs text-slate-400 block mb-1">Reconciled Budget</span>
                <span className="text-xl font-bold text-emerald-400">${Number(auditResult.total_budget_extracted).toLocaleString()}</span>
              </div>
              <div className="bg-navy-950/60 p-4 rounded-xl border border-navy-800/80">
                <span className="text-xs text-slate-400 block mb-1">Risk Flags Identified</span>
                <span className="text-xl font-bold text-brand-400">{auditResult.findings_count}</span>
              </div>
            </div>
          </div>

          {/* Color-coded Risk Flags */}
          <div className="bg-navy-900 border border-navy-800 rounded-2xl p-6">
            <h3 className="text-base font-bold text-white mb-4 flex items-center gap-2">
              <ShieldAlert className="w-5 h-5 text-brand-400" />
              Identified Compliance Findings & Remediation Advisory
            </h3>

            {auditResult.findings.length === 0 ? (
              <div className="p-6 text-center bg-emerald-500/10 border border-emerald-500/20 rounded-xl text-emerald-300 text-sm">
                No compliance infractions found! Proposal adheres to page, font, and section limits.
              </div>
            ) : (
              <div className="space-y-4">
                {auditResult.findings.map((f) => {
                  const isRed = f.severity === 'RED';
                  const isYellow = f.severity === 'YELLOW';
                  return (
                    <div 
                      key={f.id}
                      className={`p-5 rounded-xl border ${
                        isRed 
                          ? 'bg-red-500/10 border-red-500/30' 
                          : isYellow 
                          ? 'bg-amber-500/10 border-amber-500/30' 
                          : 'bg-emerald-500/10 border-emerald-500/30'
                      }`}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <span className={`text-[11px] font-extrabold uppercase px-2.5 py-0.5 rounded-full ${
                          isRed ? 'bg-red-500/20 text-red-400' : 'bg-amber-500/20 text-amber-400'
                        }`}>
                          {isRed ? 'Fatal Rejection Risk' : 'Advisory Warning'} • {f.category}
                        </span>
                      </div>
                      <p className="text-sm font-semibold text-white mb-2">{f.message}</p>
                      <div className="text-xs text-slate-300 bg-navy-950/60 p-3 rounded-lg border border-navy-800 flex items-start gap-2">
                        <span className="text-brand-400 font-bold shrink-0">Remediation:</span>
                        <span>{f.remediation_advice}</span>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            <div className="mt-6 flex justify-end">
              <button
                onClick={handleReset}
                className="inline-flex items-center gap-2 px-5 py-2.5 bg-navy-800 hover:bg-navy-700 text-slate-200 text-xs font-semibold rounded-xl border border-navy-700 transition-colors"
              >
                <RotateCcw className="w-3.5 h-3.5" />
                Submit Another Grant for Audit
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
