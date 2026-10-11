import { Shield, Sparkles, BookOpen, ExternalLink } from 'lucide-react';

export const Footer = () => {
  return (
    <footer className="bg-navy-950 border-t border-navy-800 text-slate-400 text-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8 mb-12">
          
          {/* Brand info */}
          <div className="lg:col-span-2 space-y-4">
            <div className="flex items-center gap-2.5">
              <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-brand-400 flex items-center justify-center text-white shadow-glow-brand">
                <svg className="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2">
                  <circle cx="12" cy="12" r="3" />
                  <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" />
                </svg>
              </div>
              <span className="text-xl font-bold tracking-tight text-white font-display">
                Grant<span className="text-brand-500">Lens</span>
              </span>
            </div>
            
            <p className="text-xs sm:text-sm text-slate-400 max-w-sm leading-relaxed">
              Automated pre-submission grant auditing and evaluation platform. Safeguarding high-impact scientific research from formatting and budget disqualification.
            </p>

            <div className="flex items-center gap-2 text-xs text-brand-400 font-mono">
              <span className="w-2 h-2 rounded-full bg-emerald-400" />
              <span>NSF PAPPG 24-1 & NIH SF424 Engine Online</span>
            </div>
          </div>

          {/* Platform Links */}
          <div>
            <h4 className="text-xs font-semibold text-white uppercase tracking-wider mb-4 font-mono">Platform</h4>
            <ul className="space-y-2.5 text-xs">
              <li><a href="#solicitations" className="hover:text-white transition-colors">Target Solicitations</a></li>
              <li><a href="#audit-workspace" className="hover:text-white transition-colors">Audit Workspace</a></li>
              <li><a href="#compliance-rules" className="hover:text-white transition-colors">Compliance Rules</a></li>
              <li><a href="#how-it-works" className="hover:text-white transition-colors">3-Step Workflow</a></li>
              <li><a href="#features" className="hover:text-white transition-colors">Core Capabilities</a></li>
            </ul>
          </div>

          {/* Agency Standards */}
          <div>
            <h4 className="text-xs font-semibold text-white uppercase tracking-wider mb-4 font-mono">Standards</h4>
            <ul className="space-y-2.5 text-xs">
              <li><span className="text-slate-400">NSF PAPPG 24-1 (Chapter II)</span></li>
              <li><span className="text-slate-400">NIH SF424 (R&R) Form Version H</span></li>
              <li><span className="text-slate-400">Uniform Guidance 2 CFR §200</span></li>
              <li><span className="text-slate-400">OSTP 2022 Public Access Memo</span></li>
              <li><span className="text-slate-400">DOE Office of Science Rules</span></li>
            </ul>
          </div>

          {/* Tech Stack */}
          <div>
            <h4 className="text-xs font-semibold text-white uppercase tracking-wider mb-4 font-mono">Architecture</h4>
            <ul className="space-y-2.5 text-xs">
              <li><span className="text-slate-400">Frontend: React + Vite + Tailwind</span></li>
              <li><span className="text-slate-400">Backend: Django + DRF</span></li>
              <li><span className="text-slate-400">Parser: PyMuPDF & pdfplumber</span></li>
              <li><span className="text-slate-400">Vector Store: ChromaDB</span></li>
              <li><span className="text-slate-400">AI: LangChain + Google Gemini</span></li>
            </ul>
          </div>

        </div>

        {/* Academic & Legal Disclaimer */}
        <div className="pt-8 border-t border-navy-850">
          <div className="p-4 rounded-xl bg-navy-900/60 border border-navy-800 text-xs text-slate-400 leading-relaxed space-y-2">
            <div className="flex items-center gap-1.5 text-slate-300 font-semibold">
              <Shield className="w-3.5 h-3.5 text-brand-400" />
              <span>Academic Notice & Non-Affiliation Disclaimer</span>
            </div>
            <p>
              GrantLens is an academic evaluation and pre-submission audit assistant designed to support research investigators and University Sponsored Research Offices (SROs). GrantLens is an independent evaluation tool and is not officially affiliated with, endorsed by, or sponsored by the National Science Foundation (NSF), National Institutes of Health (NIH), or any federal funding agency. Final proposal compliance and adherence to solicitation requirements remain the sole responsibility of the Principal Investigator.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 mt-8 text-xs text-slate-500">
            <p>© {new Date().getFullYear()} GrantLens. Capstone Project — All rights reserved.</p>
            <p className="font-mono">Built for academic rigor & pre-submission excellence.</p>
          </div>
        </div>

      </div>
    </footer>
  );
};
