import React from 'react';
import {
  FileText,
  ShieldAlert,
  Calculator,
  Award,
  Wand2,
  Compass,
  ArrowRight,
  Code2
} from 'lucide-react';
import { CORE_FEATURES } from '../../data/featuresData';
import { Badge } from '../ui/Badge';

const ICON_MAP = {
  FileText,
  ShieldAlert,
  Calculator,
  Award,
  Wand2,
  Compass,
};

export const FeaturesGrid = () => {
  return (
    <section id="features" className="py-16 md:py-24 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <Badge variant="brand" size="md" className="mb-3">
            Core Technology Architecture
          </Badge>
          <h2 className="text-3xl sm:text-5xl font-extrabold text-white tracking-tight font-display">
            Built for Rigorous Federal Compliance
          </h2>
          <p className="mt-4 text-base sm:text-lg text-slate-300">
            A comprehensive pipeline combining document layout parsing, vector retrieval, and LLM-driven deterministic audit checks.
          </p>
        </div>

        {/* 6 Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
          {CORE_FEATURES.map((feature) => {
            const Icon = ICON_MAP[feature.iconName] || FileText;

            return (
              <div
                key={feature.id}
                className="group relative rounded-2xl bg-navy-850/80 border border-navy-750 p-6 sm:p-7 hover:border-brand-500/50 hover:bg-navy-800/90 transition-all duration-300 shadow-lg flex flex-col justify-between"
              >
                {/* Subtle top-right glow on hover */}
                <div className="absolute top-0 right-0 w-32 h-32 bg-brand-500/0 group-hover:bg-brand-500/10 rounded-full blur-2xl transition-all duration-500 pointer-events-none" />

                <div>
                  {/* Top Bar: Icon + Tag */}
                  <div className="flex items-center justify-between mb-5">
                    <div className="w-12 h-12 rounded-xl bg-brand-500/10 border border-brand-500/30 flex items-center justify-center text-brand-400 group-hover:scale-105 group-hover:bg-brand-500/20 group-hover:text-brand-300 transition-all">
                      <Icon className="w-6 h-6" />
                    </div>
                    <span className="text-[11px] font-mono font-medium px-2.5 py-1 rounded-md bg-navy-900 border border-navy-700 text-slate-300">
                      {feature.tag}
                    </span>
                  </div>

                  {/* Title & Description */}
                  <h3 className="text-xl font-bold text-white mb-2.5 group-hover:text-brand-300 transition-colors">
                    {feature.title}
                  </h3>
                  <p className="text-sm text-slate-300 leading-relaxed mb-6">
                    {feature.description}
                  </p>
                </div>

                {/* Footer Metadata */}
                <div className="pt-4 border-t border-navy-750 space-y-2">
                  <div className="text-xs text-emerald-400 font-medium flex items-center gap-1.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                    <span>{feature.metrics}</span>
                  </div>
                  <div className="text-[11px] font-mono text-slate-400 flex items-center gap-1 truncate">
                    <Code2 className="w-3 h-3 text-slate-500 shrink-0" />
                    <span className="truncate">{feature.technicalStack}</span>
                  </div>
                </div>

              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
};
