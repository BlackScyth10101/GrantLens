import React from 'react';
import { ArrowRight, Lock, CheckCircle2, Award, FileSearch, Sparkles, AlertCircle } from 'lucide-react';
import { Button } from '../ui/Button';

export const Hero = ({ currentPersona, onCtaClick }) => {
  return (
    <section className="relative pt-12 pb-16 md:pt-20 md:pb-24 overflow-hidden">
      {/* Background radial spotlight glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[450px] bg-brand-500/10 rounded-full blur-[140px] pointer-events-none -z-10" />
      <div className="absolute top-0 right-1/4 w-[400px] h-[300px] bg-cyan-500/5 rounded-full blur-[120px] pointer-events-none -z-10" />

      <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        
        {/* Top Confidential Compliance Pill */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-navy-900/90 border border-navy-700/80 shadow-inner text-xs sm:text-sm text-slate-300 mb-8 backdrop-blur-md">
          <span className="w-2 h-2 rounded-full bg-brand-500 animate-pulse" />
          <span className="font-medium text-slate-200">Confidential Pre-Submission Compliance</span>
          <span className="text-slate-500">•</span>
          <span className="text-brand-400 font-semibold">NSF & NIH Standard</span>
        </div>

        {/* Dynamic Persona Indicator Banner */}
        {currentPersona === 'reviewer' && (
          <div className="mb-4 inline-flex items-center gap-2 px-3 py-1 rounded-md bg-purple-500/15 border border-purple-500/30 text-purple-300 text-xs">
            <Sparkles className="w-3.5 h-3.5 text-purple-400" />
            <span>Reviewer Mode Enabled: Calibrated against NSF PAPPG 24-1 Merit Review Criteria</span>
          </div>
        )}

        {/* Hero Title */}
        <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white leading-[1.1] mb-6 font-display">
          Federal-grade Grant <br className="hidden sm:inline" />
          Compliance Feedback{' '}
          <span className="relative inline-block text-transparent bg-clip-text bg-gradient-to-r from-brand-400 via-brand-500 to-amber-300">
            Instantly
            <span className="absolute left-0 -bottom-1.5 w-full h-1 bg-gradient-to-r from-brand-500 to-amber-400 rounded-full opacity-80" />
          </span>
        </h1>

        {/* Subtitle addressing the 30% desk reject problem */}
        <p className="max-w-3xl mx-auto text-base sm:text-lg lg:text-xl text-slate-300 leading-relaxed mb-4">
          Advanced AI trained on real grant solicitations to give you expert-level compliance checks, budget reconciliation, and rubric scores — <span className="text-white font-semibold underline decoration-brand-500 underline-offset-4">before you submit</span>.
        </p>

        {/* Desk rejection callout sub-badge */}
        <div className="inline-flex items-center gap-2 text-xs sm:text-sm text-slate-400 mb-8">
          <span>Meet <strong className="text-slate-200">GrantLens AI</strong> — The Pre-Submission Auditor</span>
          <span className="hidden sm:inline text-slate-600">|</span>
          <span className="hidden sm:inline-flex items-center gap-1 text-amber-400/90 font-medium">
            <AlertCircle className="w-3.5 h-3.5" />
            Preventing the 30% administrative desk-rejection rate
          </span>
        </div>

        {/* CTAs */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
          <Button
            variant="primary"
            size="pill-lg"
            icon={ArrowRight}
            iconPosition="right"
            onClick={onCtaClick}
            className="w-full sm:w-auto tracking-wide uppercase text-sm font-bold shadow-glow-brand"
          >
            Try a Free Review Now
          </Button>

          <a href="#audit-workspace">
            <Button
              variant="secondary"
              size="pill-lg"
              icon={FileSearch}
              className="w-full sm:w-auto text-sm"
            >
              Inspect Live Sample Audit
            </Button>
          </a>
        </div>

        {/* Trust & Confidence Badges */}
        <div className="flex flex-wrap items-center justify-center gap-y-3 gap-x-8 text-xs sm:text-sm text-slate-300 pt-2 border-t border-navy-800/80">
          <div className="flex items-center gap-2">
            <Lock className="w-4 h-4 text-brand-400" />
            <span>100% Confidential (Private Sandbox)</span>
          </div>

          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>Format & Budget Reconciliation</span>
          </div>

          <div className="flex items-center gap-2">
            <Award className="w-4 h-4 text-brand-400" />
            <span>0–100 Rubric Scoring</span>
          </div>
        </div>

      </div>
    </section>
  );
};
