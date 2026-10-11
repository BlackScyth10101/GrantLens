import React, { useState } from 'react';
import { Sparkles, Menu, X, GraduationCap, ShieldCheck, ChevronRight } from 'lucide-react';
import { Button } from '../ui/Button';

export const Navbar = ({ currentPersona, onPersonaChange, onLaunchAudit }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-50 w-full border-b border-navy-700/60 bg-navy-950/85 backdrop-blur-md transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-18">
          
          {/* Brand Logo */}
          <div className="flex items-center gap-3">
            <a href="#" className="flex items-center gap-2.5 group">
              <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 to-brand-400 flex items-center justify-center shadow-glow-brand group-hover:scale-105 transition-transform">
                <svg className="w-6 h-6 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                  <circle cx="12" cy="12" r="3" />
                  <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" />
                </svg>
              </div>
              <span className="text-xl font-bold tracking-tight text-white font-display">
                Grant<span className="text-brand-500">Lens</span>
              </span>
            </a>

            {/* Desktop Navigation Links */}
            <nav className="hidden lg:flex items-center ml-6 space-x-1">
              <a href="#solicitations" className="px-3 py-1.5 text-sm font-medium text-slate-300 hover:text-white hover:bg-navy-800/60 rounded-md transition-colors">
                Solicitations
              </a>
              <a href="#audit-workspace" className="px-3 py-1.5 text-sm font-medium text-slate-300 hover:text-white hover:bg-navy-800/60 rounded-md transition-colors">
                Audit Workspace
              </a>
              <a href="#compliance-rules" className="px-3 py-1.5 text-sm font-medium text-slate-300 hover:text-white hover:bg-navy-800/60 rounded-md transition-colors">
                Compliance Rules
              </a>
              <a href="#how-it-works" className="px-3 py-1.5 text-sm font-medium text-slate-300 hover:text-white hover:bg-navy-800/60 rounded-md transition-colors">
                How It Works
              </a>
            </nav>
          </div>

          {/* Right Controls: Persona Switcher + Profile + CTA */}
          <div className="hidden md:flex items-center gap-4">
            
            {/* Persona Switcher Pill */}
            <div className="flex items-center p-1 bg-navy-900 border border-navy-700 rounded-full text-xs font-medium">
              <button
                type="button"
                onClick={() => onPersonaChange('researcher')}
                className={`px-3 py-1.5 rounded-full transition-all cursor-pointer ${
                  currentPersona === 'researcher'
                    ? 'bg-slate-200 text-navy-950 font-semibold shadow-sm'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                Researcher
              </button>
              <button
                type="button"
                onClick={() => onPersonaChange('reviewer')}
                className={`px-3 py-1.5 rounded-full transition-all cursor-pointer ${
                  currentPersona === 'reviewer'
                    ? 'bg-slate-200 text-navy-950 font-semibold shadow-sm'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                Reviewer / NSF
              </button>
            </div>

            {/* Researcher Profile Badge */}
            <div className="flex items-center gap-2 px-2.5 py-1 text-xs text-brand-300 bg-brand-500/10 border border-brand-500/25 rounded-md">
              <GraduationCap className="w-3.5 h-3.5 text-brand-400" />
              <span className="font-medium">Dr. Alan Turing</span>
            </div>

            {/* Audit Proposal CTA */}
            <Button
              variant="primary"
              size="sm"
              icon={Sparkles}
              onClick={onLaunchAudit}
              className="font-semibold shadow-glow-brand"
            >
              Audit Proposal
            </Button>
          </div>

          {/* Mobile menu toggle */}
          <div className="flex items-center md:hidden gap-2">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 text-slate-400 hover:text-white rounded-lg hover:bg-navy-800"
              aria-label="Toggle menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className="md:hidden border-b border-navy-700 bg-navy-900/95 backdrop-blur-xl px-4 pt-3 pb-6 space-y-4">
          <div className="flex justify-center p-1 bg-navy-950 border border-navy-700 rounded-full text-xs font-medium w-full">
            <button
              onClick={() => { onPersonaChange('researcher'); setMobileMenuOpen(false); }}
              className={`flex-1 py-1.5 text-center rounded-full ${
                currentPersona === 'researcher' ? 'bg-slate-200 text-navy-950 font-semibold' : 'text-slate-400'
              }`}
            >
              Researcher View
            </button>
            <button
              onClick={() => { onPersonaChange('reviewer'); setMobileMenuOpen(false); }}
              className={`flex-1 py-1.5 text-center rounded-full ${
                currentPersona === 'reviewer' ? 'bg-slate-200 text-navy-950 font-semibold' : 'text-slate-400'
              }`}
            >
              Reviewer / NSF
            </button>
          </div>

          <div className="flex flex-col space-y-2">
            <a href="#solicitations" onClick={() => setMobileMenuOpen(false)} className="px-3 py-2 text-sm text-slate-300 hover:text-white hover:bg-navy-800 rounded-lg">Solicitations</a>
            <a href="#audit-workspace" onClick={() => setMobileMenuOpen(false)} className="px-3 py-2 text-sm text-slate-300 hover:text-white hover:bg-navy-800 rounded-lg">Audit Workspace</a>
            <a href="#compliance-rules" onClick={() => setMobileMenuOpen(false)} className="px-3 py-2 text-sm text-slate-300 hover:text-white hover:bg-navy-800 rounded-lg">Compliance Rules</a>
            <a href="#how-it-works" onClick={() => setMobileMenuOpen(false)} className="px-3 py-2 text-sm text-slate-300 hover:text-white hover:bg-navy-800 rounded-lg">How It Works</a>
          </div>

          <div className="pt-2">
            <Button
              variant="primary"
              size="md"
              icon={Sparkles}
              onClick={() => { onLaunchAudit(); setMobileMenuOpen(false); }}
              className="w-full justify-center"
            >
              Audit Proposal Now
            </Button>
          </div>
        </div>
      )}
    </header>
  );
};
