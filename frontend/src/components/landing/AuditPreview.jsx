import React, { useState } from 'react';
import {
  RotateCcw,
  AlertTriangle,
  AlertOctagon,
  CheckCircle2,
  TrendingUp,
  FileCheck,
  ChevronRight,
  Sparkles,
  ArrowRight,
  ExternalLink,
  ShieldCheck,
  Layers,
  FileText
} from 'lucide-react';
import { AUDIT_STATS, AUDIT_FLAGS, AUDIT_RUBRIC_BREAKDOWN } from '../../data/auditSampleData';
import { Badge } from '../ui/Badge';
import { Button } from '../ui/Button';

export const AuditPreview = () => {
  const [activeTab, setActiveTab] = useState('all');
  const [selectedFlagId, setSelectedFlagId] = useState('flag-fatal-01');
  const [isRefreshing, setIsRefreshing] = useState(false);

  const handleRefresh = () => {
    setIsRefreshing(true);
    setTimeout(() => setIsRefreshing(false), 600);
  };

  const filteredFlags = AUDIT_FLAGS.filter((flag) => {
    if (activeTab === 'all') return true;
    if (activeTab === 'fatal') return flag.severity === 'fatal';
    if (activeTab === 'warning') return flag.severity === 'warning';
    if (activeTab === 'success') return flag.severity === 'success';
    return true;
  });

  const selectedFlag = AUDIT_FLAGS.find((f) => f.id === selectedFlagId) || AUDIT_FLAGS[0];

  return (
    <section id="audit-workspace" className="relative py-12 md:py-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Heading */}
        <div className="text-center max-w-3xl mx-auto mb-10">
          <Badge variant="brand" size="md" className="mb-3">
            Simulated Pre-Submission Engine
          </Badge>
          <h2 className="text-3xl sm:text-4xl font-bold text-white tracking-tight font-display">
            Interactive Audit Workspace Preview
          </h2>
          <p className="mt-2 text-sm sm:text-base text-slate-300">
            See how GrantLens parses federal agency guidelines and proposal documents in real-time to surface compliance risks and financial discrepancies.
          </p>
        </div>

        {/* Main Application Window Card */}
        <div className="rounded-2xl border border-navy-700/80 bg-navy-900/95 shadow-2xl overflow-hidden backdrop-blur-xl">
          
          {/* Top Browser Chrome Bar */}
          <div className="flex items-center justify-between px-4 sm:px-6 py-3.5 bg-navy-950/90 border-b border-navy-800">
            <div className="flex items-center gap-2">
              <span className="w-3 h-3 rounded-full bg-red-500/80 inline-block" />
              <span className="w-3 h-3 rounded-full bg-amber-500/80 inline-block" />
              <span className="w-3 h-3 rounded-full bg-emerald-500/80 inline-block" />
            </div>

            {/* Simulated URL Pill */}
            <div className="flex items-center gap-2 px-4 py-1 rounded-md bg-navy-900 border border-navy-800 text-xs font-mono text-slate-400">
              <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block" />
              <span>app.grantlens.ai/audit-workspace</span>
            </div>

            {/* Refresh Action Button */}
            <button
              onClick={handleRefresh}
              className="flex items-center gap-1.5 text-xs text-slate-400 hover:text-slate-200 transition-colors px-2 py-1 rounded hover:bg-navy-800 cursor-pointer"
              title="Refresh simulated workspace"
            >
              <RotateCcw className={`w-3.5 h-3.5 ${isRefreshing ? 'animate-spin text-brand-400' : ''}`} />
              <span className="hidden sm:inline">Refresh</span>
            </button>
          </div>

          {/* 4 Summary Metric Tiles (Directly Matching Reference UI) */}
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 p-4 sm:p-6 bg-navy-900/50 border-b border-navy-800">
            
            {/* Tile 1: Target Solicitations */}
            <div className="p-4 rounded-xl bg-navy-850/80 border border-navy-750 hover:border-navy-600 transition-all">
              <span className="text-xs font-medium text-slate-400 block mb-1">Target Solicitations</span>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl sm:text-3xl font-extrabold text-white font-display">2</span>
              </div>
              <p className="text-xs text-brand-400 font-medium mt-1 truncate">
                NSF 24-500 • NIH R01
              </p>
            </div>

            {/* Tile 2: Proposals Ingested */}
            <div className="p-4 rounded-xl bg-navy-850/80 border border-navy-750 hover:border-navy-600 transition-all">
              <span className="text-xs font-medium text-slate-400 block mb-1">Proposals Ingested</span>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl sm:text-3xl font-extrabold text-white font-display">3</span>
              </div>
              <p className="text-xs text-slate-400 mt-1 truncate">
                Full section & table trees
              </p>
            </div>

            {/* Tile 3: Audits Completed */}
            <div className="p-4 rounded-xl bg-navy-850/80 border border-navy-750 hover:border-navy-600 transition-all">
              <span className="text-xs font-medium text-slate-400 block mb-1">Audits Completed</span>
              <div className="flex items-baseline gap-2">
                <span className="text-2xl sm:text-3xl font-extrabold text-emerald-400 font-display">2</span>
              </div>
              <p className="text-xs text-emerald-400/90 mt-1 truncate">
                100% evaluated
              </p>
            </div>

            {/* Tile 4: Average Rubric Score */}
            <div className="p-4 rounded-xl bg-navy-850/80 border border-navy-750 hover:border-brand-500/50 transition-all relative overflow-hidden group">
              <span className="text-xs font-medium text-slate-400 block mb-1">Average Rubric Score</span>
              <div className="flex items-baseline gap-1.5">
                <span className="text-2xl sm:text-3xl font-extrabold text-white font-display">96.2</span>
                <span className="text-sm text-slate-400 font-semibold">/ 100</span>
              </div>
              <div className="flex items-center gap-1 text-xs text-emerald-400 font-medium mt-1">
                <TrendingUp className="w-3.5 h-3.5" />
                <span>High compliance fidelity</span>
              </div>
            </div>

          </div>

          {/* Interactive Audit Findings Explorer */}
          <div className="p-4 sm:p-6">
            
            {/* Filter Tabs */}
            <div className="flex flex-wrap items-center justify-between gap-3 mb-6 pb-4 border-b border-navy-800">
              <div className="flex items-center gap-2">
                <span className="text-xs font-semibold uppercase tracking-wider text-slate-400 mr-2">Audit Stream:</span>
                <button
                  onClick={() => setActiveTab('all')}
                  className={`px-3 py-1 text-xs font-medium rounded-lg transition-all cursor-pointer ${
                    activeTab === 'all'
                      ? 'bg-brand-500 text-white font-semibold shadow-glow-brand'
                      : 'bg-navy-800 text-slate-300 hover:text-white'
                  }`}
                >
                  All Findings (6)
                </button>
                <button
                  onClick={() => setActiveTab('fatal')}
                  className={`px-3 py-1 text-xs font-medium rounded-lg transition-all flex items-center gap-1.5 cursor-pointer ${
                    activeTab === 'fatal'
                      ? 'bg-red-500 text-white font-semibold shadow-glow-fatal'
                      : 'bg-red-500/10 text-red-400 hover:bg-red-500/20'
                  }`}
                >
                  <AlertOctagon className="w-3 h-3" />
                  Fatal Violations (1)
                </button>
                <button
                  onClick={() => setActiveTab('warning')}
                  className={`px-3 py-1 text-xs font-medium rounded-lg transition-all flex items-center gap-1.5 cursor-pointer ${
                    activeTab === 'warning'
                      ? 'bg-amber-500 text-white font-semibold'
                      : 'bg-amber-500/10 text-amber-400 hover:bg-amber-500/20'
                  }`}
                >
                  <AlertTriangle className="w-3 h-3" />
                  Warnings (2)
                </button>
                <button
                  onClick={() => setActiveTab('success')}
                  className={`px-3 py-1 text-xs font-medium rounded-lg transition-all flex items-center gap-1.5 cursor-pointer ${
                    activeTab === 'success'
                      ? 'bg-emerald-500 text-white font-semibold shadow-glow-success'
                      : 'bg-emerald-500/10 text-emerald-400 hover:bg-emerald-500/20'
                  }`}
                >
                  <CheckCircle2 className="w-3 h-3" />
                  Compliant Gates (3)
                </button>
              </div>

              <span className="text-xs text-slate-400 font-mono hidden md:inline">
                Target: NSF CISE 24-500 §II.D
              </span>
            </div>

            {/* Split Screen Inspector: Left Findings List, Right Detailed Diagnostic */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
              
              {/* Left Column: Finding Cards */}
              <div className="lg:col-span-5 space-y-3 max-h-[460px] overflow-y-auto pr-1">
                {filteredFlags.map((flag) => {
                  const isSelected = flag.id === selectedFlag.id;
                  return (
                    <div
                      key={flag.id}
                      onClick={() => setSelectedFlagId(flag.id)}
                      className={`p-3.5 rounded-xl border transition-all cursor-pointer text-left ${
                        isSelected
                          ? flag.severity === 'fatal'
                            ? 'bg-red-950/30 border-red-500/60 shadow-glow-fatal'
                            : flag.severity === 'warning'
                            ? 'bg-amber-950/30 border-amber-500/60'
                            : 'bg-emerald-950/30 border-emerald-500/60 shadow-glow-success'
                          : 'bg-navy-850/60 border-navy-750 hover:border-navy-600 hover:bg-navy-800'
                      }`}
                    >
                      <div className="flex items-start justify-between gap-2 mb-1.5">
                        <span className="font-mono text-xs px-2 py-0.5 rounded bg-navy-900 border border-navy-700 text-slate-300">
                          {flag.code}
                        </span>
                        <span className={`text-[11px] font-semibold uppercase px-2 py-0.5 rounded-full ${
                          flag.severity === 'fatal'
                            ? 'bg-red-500/20 text-red-400 border border-red-500/30'
                            : flag.severity === 'warning'
                            ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                            : 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                        }`}>
                          {flag.severity === 'fatal' ? 'Fatal Desk-Reject' : flag.severity === 'warning' ? 'Budget Warning' : 'Passed Check'}
                        </span>
                      </div>

                      <h4 className="text-sm font-semibold text-white leading-snug line-clamp-1">
                        {flag.title}
                      </h4>
                      <p className="text-xs text-slate-400 mt-1 line-clamp-2">
                        {flag.description}
                      </p>

                      <div className="flex items-center justify-between text-[11px] text-slate-400 mt-2.5 pt-2 border-t border-navy-800/80">
                        <span className="truncate">{flag.section}</span>
                        <ChevronRight className="w-3.5 h-3.5 text-slate-400 shrink-0" />
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Right Column: Deep Diagnostic Inspector */}
              <div className="lg:col-span-7 bg-navy-850/90 border border-navy-700/80 rounded-xl p-5 flex flex-col justify-between">
                <div>
                  
                  {/* Card Header */}
                  <div className="flex items-center justify-between pb-3 border-b border-navy-750 mb-4">
                    <div className="flex items-center gap-2">
                      <span className={`w-2.5 h-2.5 rounded-full ${
                        selectedFlag.severity === 'fatal' ? 'bg-red-500 animate-pulse' : selectedFlag.severity === 'warning' ? 'bg-amber-500' : 'bg-emerald-500'
                      }`} />
                      <span className="text-xs font-mono font-medium text-slate-300">
                        Diagnostic Node: {selectedFlag.code}
                      </span>
                    </div>
                    <span className="text-xs text-slate-400 font-medium">
                      Agency: {selectedFlag.agency}
                    </span>
                  </div>

                  {/* Title & Section */}
                  <h3 className="text-lg font-bold text-white mb-2">
                    {selectedFlag.title}
                  </h3>
                  <div className="text-xs text-brand-400 font-medium mb-4 flex items-center gap-1.5">
                    <Layers className="w-3.5 h-3.5" />
                    <span>Location: {selectedFlag.section}</span>
                  </div>

                  {/* Evidence Box */}
                  <div className="p-3.5 rounded-lg bg-navy-900 border border-navy-750 mb-4 text-xs">
                    <span className="font-semibold text-slate-200 block mb-1">Extracted Document Evidence:</span>
                    <p className="text-slate-300 font-mono leading-relaxed">
                      "{selectedFlag.evidence}"
                    </p>
                  </div>

                  {/* Actionable Remediation or Pass Confirmation */}
                  {selectedFlag.recommendation ? (
                    <div className="p-3.5 rounded-lg bg-brand-500/10 border border-brand-500/30 mb-4 text-xs">
                      <div className="flex items-center gap-1.5 text-brand-400 font-semibold mb-1">
                        <Sparkles className="w-4 h-4" />
                        <span>GrantLens AI Targeted Remediation:</span>
                      </div>
                      <p className="text-slate-300 leading-relaxed">
                        {selectedFlag.recommendation}
                      </p>
                    </div>
                  ) : (
                    <div className="p-3.5 rounded-lg bg-emerald-500/10 border border-emerald-500/30 mb-4 text-xs">
                      <div className="flex items-center gap-1.5 text-emerald-400 font-semibold mb-1">
                        <CheckCircle2 className="w-4 h-4" />
                        <span>Rule Fully Verified:</span>
                      </div>
                      <p className="text-slate-300 leading-relaxed">
                        Meets strict federal formatting and mandatory heading guidelines. No remediation necessary.
                      </p>
                    </div>
                  )}

                  {/* Impact Summary */}
                  <div className="text-xs text-slate-400 flex items-center justify-between">
                    <span>Outcome Impact: <strong className="text-slate-200">{selectedFlag.impact}</strong></span>
                  </div>

                </div>

                {/* Footer Action */}
                <div className="pt-4 mt-4 border-t border-navy-750 flex items-center justify-between">
                  <div className="text-xs text-slate-400 font-mono">
                    Evaluation confidence: <span className="text-emerald-400 font-semibold">99.8%</span>
                  </div>
                  <Button
                    variant="primary"
                    size="sm"
                    icon={Sparkles}
                    className="text-xs"
                    onClick={() => alert(`Simulating AI rewrite engine for rule: ${selectedFlag.code}`)}
                  >
                    Simulate AI Rewrite
                  </Button>
                </div>

              </div>

            </div>

          </div>

        </div>

      </div>
    </section>
  );
};
