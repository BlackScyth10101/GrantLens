import React, { useState } from 'react';
import {
  AlertOctagon,
  AlertTriangle,
  CheckCircle2,
  Sparkles,
  ArrowRight,
  FileCheck2,
  FileSpreadsheet,
  Scissors,
  Check,
  Split
} from 'lucide-react';
import { Badge } from '../ui/Badge';
import { Button } from '../ui/Button';

export const FlagShowcase = () => {
  const [selectedExample, setSelectedExample] = useState('fatal');

  const examples = {
    fatal: {
      type: 'fatal',
      badge: 'Fatal Desk-Reject Error',
      ruleCode: 'NSF PAPPG 24-1 §II.D.2.d(i)',
      agency: 'NSF 24-500 CISE Core Program',
      title: 'Project Description Overflow: 15.4 / 15.0 Pages',
      impactText: 'Immediate Administrative Return Without Review',
      problem: 'PyMuPDF extracted 15.4 total pages for the Project Description. An overflow of 410 words across Section 3.2 and Section 4.1 exceeds the strict statutory ceiling.',
      diffBefore: 'Traditional approaches suffer from latency bottlenecks during real-time feature extraction in distributed clusters (Smith et al., 2021). Our proposed framework fundamentally restructures the inter-node communication pipeline through dynamic topology discovery, ensuring that downstream aggregation tasks experience deterministic throughput even under severe packet loss or unpredictable node failures.',
      diffAfter: 'Traditional architectures encounter latency bottlenecks during distributed feature extraction (Smith et al., 2021). Our framework streamlines inter-node communication via dynamic topology discovery, guaranteeing deterministic throughput despite packet loss or node failures.',
      savings: 'Trimmed 28 words (36% reduction) while preserving core technical mechanism and citation.',
    },
    warning: {
      type: 'warning',
      badge: 'Financial Reconciliation Warning',
      ruleCode: '2 CFR §200 Uniform Guidance',
      agency: 'NIH R01 PA-20-185 & NSF Combined',
      title: 'Narrative vs. Table 2 Postdoctoral Effort Discrepancy',
      impactText: 'Reviewer Scoring Penalty & Post-Award Budget Audit Hold',
      problem: 'pdfplumber parsed Table 2 (Personnel Costs) reflecting 2.0 person-months ($34,200). However, Section 6.2 Budget Justification narrative states: "Postdoctoral Researcher will dedicate 1.5 person-months ($25,650)".',
      diffBefore: 'The Senior Postdoctoral Scholar will dedicate 1.5 person-months ($25,650) to Aim 2 algorithm validation and benchmarking...',
      diffAfter: 'The Senior Postdoctoral Scholar will dedicate 2.0 person-months ($34,200) to Aim 2 algorithm validation and benchmarking (consistent with Table 2 Personnel allocations)...',
      savings: 'Reconciled narrative figure with audited financial table to the exact dollar.',
    },
    success: {
      type: 'success',
      badge: 'Passed Compliance Gate',
      ruleCode: 'NSF PAPPG Chapter II.D.2.d',
      agency: 'National Science Foundation Standard',
      title: 'Standalone "Broader Impacts" & "Intellectual Merit" Verified',
      impactText: '100% Compliant — Full Clearance to Peer Review Panel',
      problem: 'Mandatory structural verification passed. Both required headings exist as isolated H2 headers with compliant text margins and typographic hierarchy.',
      diffBefore: null,
      diffAfter: 'Detected Standalone Header: "Broader Impacts" on Page 13, Paragraph 4. Font: Arial 10pt Bold. Content: Education outreach, underrepresented STEM participation, open-source dataset release.',
      savings: 'All 14 structural compliance criteria verified.',
    }
  };

  const current = examples[selectedExample];

  return (
    <section id="compliance-rules" className="py-16 md:py-24 relative overflow-hidden bg-navy-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-14">
          <Badge variant="brand" size="md" className="mb-3">
            Real Agency Violations & Fixes
          </Badge>
          <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-display">
            Color-Coded Compliance Flags in Action
          </h2>
          <p className="mt-4 text-base sm:text-lg text-slate-300">
            Explore how GrantLens identifies fatal administrative errors, cross-reconciles budget tables, and provides grounded rewrite recommendations.
          </p>
        </div>

        {/* Flag Selector Tabs */}
        <div className="flex flex-wrap items-center justify-center gap-3 mb-10">
          <button
            onClick={() => setSelectedExample('fatal')}
            className={`flex items-center gap-2 px-5 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              selectedExample === 'fatal'
                ? 'bg-red-500 text-white shadow-glow-fatal'
                : 'bg-navy-900 text-slate-400 hover:text-slate-200 border border-navy-800'
            }`}
          >
            <AlertOctagon className="w-4 h-4" />
            <span>Red: Fatal Errors (Page Cap Overflow)</span>
          </button>

          <button
            onClick={() => setSelectedExample('warning')}
            className={`flex items-center gap-2 px-5 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              selectedExample === 'warning'
                ? 'bg-amber-500 text-navy-950 shadow-md font-bold'
                : 'bg-navy-900 text-slate-400 hover:text-slate-200 border border-navy-800'
            }`}
          >
            <AlertTriangle className="w-4 h-4" />
            <span>Yellow: Warnings (Budget Discrepancies)</span>
          </button>

          <button
            onClick={() => setSelectedExample('success')}
            className={`flex items-center gap-2 px-5 py-2.5 rounded-full text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
              selectedExample === 'success'
                ? 'bg-emerald-500 text-white shadow-glow-success'
                : 'bg-navy-900 text-slate-400 hover:text-slate-200 border border-navy-800'
            }`}
          >
            <CheckCircle2 className="w-4 h-4" />
            <span>Green: Passed Checks (Verified Headings)</span>
          </button>
        </div>

        {/* Diagnostic Banner Card */}
        <div className={`rounded-2xl border p-6 sm:p-8 transition-all ${
          current.type === 'fatal'
            ? 'bg-navy-900/90 border-red-500/40 shadow-glow-fatal/20'
            : current.type === 'warning'
            ? 'bg-navy-900/90 border-amber-500/40'
            : 'bg-navy-900/90 border-emerald-500/40 shadow-glow-success/20'
        }`}>
          
          {/* Card Header */}
          <div className="flex flex-wrap items-center justify-between gap-3 pb-6 border-b border-navy-750 mb-6">
            <div className="flex items-center gap-3">
              <span className={`p-2 rounded-xl ${
                current.type === 'fatal' ? 'bg-red-500/20 text-red-400' : current.type === 'warning' ? 'bg-amber-500/20 text-amber-400' : 'bg-emerald-500/20 text-emerald-400'
              }`}>
                {current.type === 'fatal' && <AlertOctagon className="w-6 h-6" />}
                {current.type === 'warning' && <AlertTriangle className="w-6 h-6" />}
                {current.type === 'success' && <CheckCircle2 className="w-6 h-6" />}
              </span>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs text-slate-400">{current.ruleCode}</span>
                  <span className="text-slate-600">•</span>
                  <span className="text-xs text-brand-400 font-medium">{current.agency}</span>
                </div>
                <h3 className="text-lg sm:text-xl font-bold text-white mt-0.5">{current.title}</h3>
              </div>
            </div>

            <span className={`text-xs font-bold px-3 py-1.5 rounded-full ${
              current.type === 'fatal'
                ? 'bg-red-500/20 text-red-300 border border-red-500/40'
                : current.type === 'warning'
                ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                : 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
            }`}>
              {current.badge}
            </span>
          </div>

          {/* Diagnostic Context */}
          <div className="mb-6">
            <h4 className="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">
              Audit Detection & Risk:
            </h4>
            <p className="text-sm sm:text-base text-slate-200 leading-relaxed">
              {current.problem}
            </p>
            <div className="mt-2 text-xs font-semibold flex items-center gap-1.5 text-slate-400">
              <span>Impact:</span>
              <span className={current.type === 'fatal' ? 'text-red-400' : current.type === 'warning' ? 'text-amber-400' : 'text-emerald-400'}>
                {current.impactText}
              </span>
            </div>
          </div>

          {/* Before & After Diff Box (if fatal or warning) */}
          {current.diffBefore ? (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 rounded-xl bg-navy-950 p-4 border border-navy-800">
              
              {/* Before */}
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs text-red-400 font-semibold pb-1 border-b border-navy-800">
                  <span>Flagged Proposal Draft Text</span>
                  <span className="font-mono">Non-compliant</span>
                </div>
                <p className="text-xs text-slate-400 font-mono leading-relaxed bg-red-950/20 p-3 rounded border border-red-900/30">
                  {current.diffBefore}
                </p>
              </div>

              {/* After */}
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs text-emerald-400 font-semibold pb-1 border-b border-navy-800">
                  <div className="flex items-center gap-1">
                    <Sparkles className="w-3.5 h-3.5" />
                    <span>GrantLens AI Targeted Rewrite</span>
                  </div>
                  <span className="font-mono">Verified Compliant</span>
                </div>
                <p className="text-xs text-slate-200 font-mono leading-relaxed bg-emerald-950/20 p-3 rounded border border-emerald-900/30">
                  {current.diffAfter}
                </p>
              </div>

            </div>
          ) : (
            <div className="rounded-xl bg-emerald-950/20 border border-emerald-900/30 p-4">
              <div className="flex items-center gap-2 text-emerald-400 text-xs font-semibold mb-1">
                <Check className="w-4 h-4" />
                <span>Verification Diagnostic Stream</span>
              </div>
              <p className="text-xs text-slate-300 font-mono leading-relaxed">
                {current.diffAfter}
              </p>
            </div>
          )}

          {/* Footer Savings Callout */}
          <div className="mt-4 pt-4 border-t border-navy-750 flex flex-wrap items-center justify-between gap-2 text-xs">
            <span className="text-slate-400">
              Audit Result: <strong className="text-slate-200">{current.savings}</strong>
            </span>
            <span className="text-brand-400 font-mono">
              Deterministic rule match • zero hallucination
            </span>
          </div>

        </div>

      </div>
    </section>
  );
};
