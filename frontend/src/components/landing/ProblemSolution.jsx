import React from 'react';
import { XCircle, CheckCircle2, Clock, AlertTriangle, Zap, ShieldCheck } from 'lucide-react';
import { COMPARISON_DATA } from '../../data/featuresData';
import { Badge } from '../ui/Badge';

export const ProblemSolution = () => {
  return (
    <section className="py-16 md:py-24 relative overflow-hidden bg-navy-900/60 border-y border-navy-800/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <Badge variant="brand" size="md" className="mb-3">
            Why Pre-Submission Auditing Matters
          </Badge>
          <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-display">
            The Cost of Manual Review Friction
          </h2>
          <p className="mt-4 text-base sm:text-lg text-slate-300">
            Every year, thousands of world-class scientific proposals are returned without review due to minor administrative oversights. Compare the traditional nightmare with GrantLens automated auditing.
          </p>
        </div>

        {/* Side by Side Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10">
          
          {/* Card 1: Manual Review Friction (Red Accent) */}
          <div className="rounded-2xl bg-navy-850/80 border border-red-500/25 p-6 sm:p-8 relative overflow-hidden shadow-lg">
            <div className="absolute top-0 right-0 w-64 h-64 bg-red-500/5 rounded-full blur-3xl pointer-events-none" />
            
            <div className="flex items-center justify-between pb-6 border-b border-navy-750 mb-6">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-red-500/15 border border-red-500/30 flex items-center justify-center text-red-400">
                  <Clock className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-white">Manual Grant Preparation</h3>
                  <span className="text-xs text-red-400 font-medium">High Risk • 40+ Hours of Fatigue</span>
                </div>
              </div>
              <span className="text-xs font-semibold px-2.5 py-1 rounded bg-red-500/15 text-red-300 border border-red-500/30">
                Current Reality
              </span>
            </div>

            <ul className="space-y-4">
              {COMPARISON_DATA.manual.map((item, idx) => (
                <li key={idx} className="flex items-start gap-3 p-3.5 rounded-xl bg-navy-900/60 border border-navy-750/80">
                  <XCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-sm font-semibold text-slate-200">{item.label}</h4>
                    <p className="text-xs sm:text-sm text-slate-400 mt-0.5 leading-relaxed">{item.text}</p>
                  </div>
                </li>
              ))}
            </ul>
          </div>

          {/* Card 2: GrantLens Automated Auditing (Brand Emerald/Orange Accent) */}
          <div className="rounded-2xl bg-navy-850/90 border border-brand-500/40 p-6 sm:p-8 relative overflow-hidden shadow-glow-brand/20">
            <div className="absolute top-0 right-0 w-64 h-64 bg-brand-500/10 rounded-full blur-3xl pointer-events-none" />

            <div className="flex items-center justify-between pb-6 border-b border-navy-750 mb-6">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-brand-500/15 border border-brand-500/40 flex items-center justify-center text-brand-400">
                  <Zap className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-white">GrantLens AI Audit Pipeline</h3>
                  <span className="text-xs text-emerald-400 font-medium">30-Second Verification • 100% Grounded</span>
                </div>
              </div>
              <span className="text-xs font-semibold px-2.5 py-1 rounded bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                GrantLens Standard
              </span>
            </div>

            <ul className="space-y-4">
              {COMPARISON_DATA.automated.map((item, idx) => (
                <li key={idx} className="flex items-start gap-3 p-3.5 rounded-xl bg-navy-900/90 border border-brand-500/20 hover:border-brand-500/40 transition-colors">
                  <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                  <div>
                    <h4 className="text-sm font-semibold text-white">{item.label}</h4>
                    <p className="text-xs sm:text-sm text-slate-300 mt-0.5 leading-relaxed">{item.text}</p>
                  </div>
                </li>
              ))}
            </ul>
          </div>

        </div>

      </div>
    </section>
  );
};
