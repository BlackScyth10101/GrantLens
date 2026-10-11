import React from 'react';
import { UploadCloud, Cpu, FileCheck, ArrowRight, Check } from 'lucide-react';
import { WORKFLOW_STEPS } from '../../data/featuresData';
import { Badge } from '../ui/Badge';

const STEP_ICONS = [UploadCloud, Cpu, FileCheck];

export const HowItWorks = () => {
  return (
    <section id="how-it-works" className="py-16 md:py-24 relative bg-navy-900/40 border-t border-navy-800/80">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <Badge variant="brand" size="md" className="mb-3">
            Simple 3-Step Workflow
          </Badge>
          <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-display">
            From Raw PDF to Submission-Ready Dossier
          </h2>
          <p className="mt-4 text-base sm:text-lg text-slate-300">
            GrantLens removes the anxiety from federal grant submissions through automated, end-to-end pre-submission auditing.
          </p>
        </div>

        {/* 3 Step Pipeline Cards */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 relative">
          
          {WORKFLOW_STEPS.map((step, idx) => {
            const Icon = STEP_ICONS[idx] || UploadCloud;

            return (
              <div
                key={step.step}
                className="relative rounded-2xl bg-navy-850/90 border border-navy-750 p-6 sm:p-8 flex flex-col justify-between hover:border-brand-500/40 transition-all shadow-xl group"
              >
                {/* Step Number Accent Badge */}
                <div className="flex items-center justify-between mb-6">
                  <div className="w-12 h-12 rounded-xl bg-gradient-to-tr from-brand-600 to-brand-400 flex items-center justify-center text-white font-bold shadow-glow-brand">
                    <Icon className="w-6 h-6" />
                  </div>
                  <span className="font-mono text-3xl font-extrabold text-navy-700 group-hover:text-brand-500/40 transition-colors">
                    {step.step}
                  </span>
                </div>

                {/* Content */}
                <div className="flex-1">
                  <span className="text-xs font-semibold text-brand-400 uppercase tracking-wider block mb-1">
                    {step.subtitle}
                  </span>
                  <h3 className="text-xl font-bold text-white mb-3">
                    {step.title}
                  </h3>
                  <p className="text-sm text-slate-300 leading-relaxed mb-6">
                    {step.description}
                  </p>

                  {/* Bullet points */}
                  <ul className="space-y-2.5 mb-6">
                    {step.bullets.map((bullet, bIdx) => (
                      <li key={bIdx} className="flex items-start gap-2.5 text-xs text-slate-300">
                        <Check className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                        <span>{bullet}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                {/* Footer Badge */}
                <div className="pt-4 border-t border-navy-750">
                  <span className="inline-block text-xs font-mono font-medium px-2.5 py-1 rounded bg-navy-900 border border-navy-700 text-slate-300">
                    Engine: {step.badge}
                  </span>
                </div>

              </div>
            );
          })}

        </div>

      </div>
    </section>
  );
};
