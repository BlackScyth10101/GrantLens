/**
 * =============================================================================
 * GrantLens Frontend - Master Application Component (src/App.jsx)
 * =============================================================================
 * Project: GrantLens - AI Grant Auditing & Evaluation Platform
 * Scope: Week 2 Milestone - Full Stack Auth, Dual PDF Ingestion & Compliance Engine
 * =============================================================================
 */

import React, { useState, useEffect } from 'react';

// Lucide React SVG Icons
import { 
  Sparkles,       
  ArrowRight,     
  Lock,           
  CheckCircle2,   
  Award,          
  Upload,         
  TrendingUp,     
  RefreshCw,      
  FileText,
  UserCheck,
  ShieldCheck,
  LayoutDashboard
} from 'lucide-react';

import AuthPortal from './components/portal/AuthPortal';
import SubmissionPortal from './components/portal/SubmissionPortal';

function App() {
  // Navigation / View state: 'landing' | 'auth' | 'portal'
  const [currentView, setCurrentView] = useState('landing');
  
  // Authenticated user state
  const [currentUser, setCurrentUser] = useState(() => {
    try {
      const saved = localStorage.getItem('grantlens_user');
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  });

  const [authToken, setAuthToken] = useState(() => {
    return localStorage.getItem('grantlens_token') || null;
  });

  // Backend telemetry status
  const [backendStatus, setBackendStatus] = useState({
    connected: false,
    loading: true,
    data: null,
  });

  // Non-blocking asynchronous network request to fetch platform metrics
  const checkBackend = async () => {
    try {
      // First try FastAPI v1 endpoint, then fallback to legacy status
      let response = await fetch('http://127.0.0.1:8000/api/v1/status');
      if (!response.ok) {
        response = await fetch('http://127.0.0.1:8000/api/status/');
      }
      
      if (response.ok) {
        const data = await response.json();
        setBackendStatus({
          connected: true,
          loading: false,
          data,
        });
      } else {
        setBackendStatus({ connected: false, loading: false, data: null });
      }
    } catch {
      setBackendStatus({ connected: false, loading: false, data: null });
    }
  };

  useEffect(() => {
    checkBackend();
  }, []);

  const handleAuthSuccess = (user, token) => {
    setCurrentUser(user);
    setAuthToken(token);
    setCurrentView('portal');
  };

  const handleSignOut = () => {
    localStorage.removeItem('grantlens_token');
    localStorage.removeItem('grantlens_user');
    setCurrentUser(null);
    setAuthToken(null);
    setCurrentView('landing');
  };

  const handleEnterWorkspace = () => {
    if (currentUser && authToken) {
      setCurrentView('portal');
    } else {
      setCurrentView('auth');
    }
  };

  const stats = backendStatus.data || {
    solicitations_count: 2,
    solicitations_detail: "NSF 24-500 • NIH R01",
    proposals_count: 3,
    proposals_detail: "Full section & table trees",
    audits_completed: 2,
    audits_detail: "100% evaluated",
    average_score: 96.2,
    score_detail: "High compliance fidelity",
    timestamp: "Live",
  };

  return (
    <div className="min-h-screen bg-[#070A12] text-slate-100 flex flex-col font-sans selection:bg-brand-500 selection:text-white">
      
      {/* =====================================================================
          GLOBAL NAVIGATION BAR
          ===================================================================== */}
      <nav className="border-b border-slate-800/80 bg-[#070A12]/90 backdrop-blur-md sticky top-0 z-50">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
          
          {/* Brand Logo */}
          <button 
            onClick={() => setCurrentView('landing')}
            className="flex items-center gap-2.5 text-left cursor-pointer bg-transparent border-0"
          >
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-brand-500 flex items-center justify-center shadow-md shadow-brand-500/20">
              <ShieldCheck className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-bold tracking-tight text-white">
              Grant<span className="text-brand-500">Lens</span>
            </span>
          </button>

          {/* Simple Navigation Anchor Links */}
          <div className="hidden md:flex items-center gap-6 text-sm text-slate-300">
            <button 
              onClick={() => setCurrentView('landing')} 
              className={`hover:text-white transition-colors cursor-pointer ${currentView === 'landing' ? 'text-white font-semibold' : ''}`}
            >
              Overview
            </button>
            <button 
              onClick={handleEnterWorkspace} 
              className={`hover:text-white transition-colors cursor-pointer ${currentView === 'portal' ? 'text-white font-semibold' : ''}`}
            >
              Audit Workspace
            </button>
          </div>

          {/* Right Controls: Connection Badge + Portal Access */}
          <div className="flex items-center gap-3">
            
            {/* Live Backend Status Pill */}
            <div className={`flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium border ${
              backendStatus.connected
                ? 'bg-emerald-950/30 text-emerald-400 border-emerald-500/40'
                : 'bg-slate-900 text-slate-400 border-slate-700'
            }`}>
              <span className={`w-2 h-2 rounded-full ${
                backendStatus.connected ? 'bg-emerald-400 animate-pulse' : 'bg-slate-500'
              }`} />
              <span className="hidden sm:inline">Engine:</span>
              <span>{backendStatus.connected ? 'FastAPI 2.0 (Online)' : 'Connecting...'}</span>
            </div>

            {/* User Auth or Workspace Trigger */}
            {currentUser ? (
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setCurrentView('portal')}
                  className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-navy-800 hover:bg-navy-750 text-white text-xs sm:text-sm font-semibold transition-all border border-navy-700 cursor-pointer"
                >
                  <UserCheck className="w-3.5 h-3.5 text-emerald-400" />
                  <span className="hidden sm:inline">{currentUser.full_name.split(' ')[0]}</span>
                  <span>Portal</span>
                </button>
              </div>
            ) : (
              <button
                onClick={() => setCurrentView(currentView === 'auth' ? 'landing' : 'auth')}
                className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-brand-500 hover:bg-brand-600 text-slate-950 text-xs sm:text-sm font-bold transition-all shadow-md shadow-brand-500/20 cursor-pointer"
              >
                <Sparkles className="w-3.5 h-3.5" />
                <span>{currentView === 'auth' ? 'Public View' : 'Researcher Sign In'}</span>
              </button>
            )}
          </div>

        </div>
      </nav>

      {/* =====================================================================
          VIEW ROUTER
          ===================================================================== */}
      {currentView === 'auth' && (
        <AuthPortal 
          onAuthSuccess={handleAuthSuccess} 
          onCancel={() => setCurrentView('landing')} 
        />
      )}

      {currentView === 'portal' && (
        <SubmissionPortal 
          user={currentUser} 
          token={authToken} 
          onSignOut={handleSignOut} 
        />
      )}

      {currentView === 'landing' && (
        <>
          {/* HERO SECTION */}
          <section id="overview" className="pt-16 pb-12 sm:pt-20 sm:pb-16 text-center px-4 max-w-4xl mx-auto">
            
            {/* Compliance Standard Badge */}
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/90 border border-slate-800 text-xs sm:text-sm text-slate-300 mb-6">
              <span className="w-2 h-2 rounded-full bg-brand-500 animate-pulse" />
              <span>Confidential Pre-Submission Compliance</span>
              <span className="text-slate-600">•</span>
              <span className="text-brand-400 font-medium">NSF & NIH Standard</span>
            </div>

            {/* Primary Headline */}
            <h1 className="text-4xl sm:text-6xl font-extrabold text-white tracking-tight leading-[1.15] mb-6">
              Federal-grade Grant <br />
              Compliance Feedback{' '}
              <span className="text-brand-500 underline decoration-brand-500/50 underline-offset-8">
                Instantly
              </span>
            </h1>

            {/* Subtitle */}
            <p className="text-base sm:text-lg text-slate-300 max-w-2xl mx-auto mb-8 leading-relaxed">
              Automated geometry analysis, margin verification, font sizing, and budget line-item reconciliation using PyMuPDF and pdfplumber — before SRO sign-off.
            </p>

            {/* Main Call to Action Button */}
            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 mb-10">
              <button
                onClick={handleEnterWorkspace}
                className="flex items-center gap-2 px-6 py-3 rounded-full bg-brand-500 hover:bg-brand-400 text-slate-950 font-bold text-sm sm:text-base transition-all shadow-lg shadow-brand-500/25 cursor-pointer uppercase tracking-wider"
              >
                <span>Launch Compliance Portal</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>

            {/* Trust Badges */}
            <div className="flex flex-wrap items-center justify-center gap-y-2 gap-x-8 text-xs sm:text-sm text-slate-400">
              <div className="flex items-center gap-2">
                <Lock className="w-4 h-4 text-brand-400" />
                <span>100% Confidential</span>
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

          </section>

          {/* PLATFORM PREVIEW WINDOW */}
          <section id="workspace" className="max-w-5xl mx-auto px-4 sm:px-6 pb-20 w-full">
            <div className="rounded-2xl border border-slate-800 bg-[#0B0F19] shadow-2xl overflow-hidden">
              
              {/* Mock Browser Header */}
              <div className="flex items-center justify-between px-4 py-3 bg-[#070A12] border-b border-slate-800">
                <div className="flex items-center gap-2">
                  <span className="w-3 h-3 rounded-full bg-red-500/80 inline-block" />
                  <span className="w-3 h-3 rounded-full bg-amber-500/80 inline-block" />
                  <span className="w-3 h-3 rounded-full bg-emerald-500/80 inline-block" />
                </div>

                <div className="flex items-center gap-2 px-3 py-1 rounded bg-[#0B0F19] border border-slate-800 text-xs font-mono text-slate-400">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block" />
                  <span>app.grantlens.ai/audit-workspace</span>
                </div>

                <button
                  onClick={checkBackend}
                  className="text-xs text-slate-400 hover:text-slate-200 flex items-center gap-1 cursor-pointer"
                  title="Sync with Backend"
                >
                  <RefreshCw className="w-3.5 h-3.5" />
                  <span className="hidden sm:inline">Refresh</span>
                </button>
              </div>

              {/* 4 LIVE METRIC TILES */}
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 p-5 sm:p-6 border-b border-slate-800 bg-[#0F1626]/50">
                
                {/* Tile 1 */}
                <div className="p-4 rounded-xl bg-[#141E34]/80 border border-slate-800">
                  <span className="text-xs text-slate-400 block mb-1">Target Solicitations</span>
                  <span className="text-2xl font-extrabold text-white">{stats.solicitations_count}</span>
                  <p className="text-xs text-brand-400 font-medium mt-1 truncate">{stats.solicitations_detail}</p>
                </div>

                {/* Tile 2 */}
                <div className="p-4 rounded-xl bg-[#141E34]/80 border border-slate-800">
                  <span className="text-xs text-slate-400 block mb-1">Proposals Ingested</span>
                  <span className="text-2xl font-extrabold text-white">{stats.proposals_count}</span>
                  <p className="text-xs text-slate-400 mt-1 truncate">{stats.proposals_detail}</p>
                </div>

                {/* Tile 3 */}
                <div className="p-4 rounded-xl bg-[#141E34]/80 border border-slate-800">
                  <span className="text-xs text-slate-400 block mb-1">Audits Completed</span>
                  <span className="text-2xl font-extrabold text-emerald-400">{stats.audits_completed}</span>
                  <p className="text-xs text-emerald-400/90 mt-1 truncate">{stats.audits_detail}</p>
                </div>

                {/* Tile 4 */}
                <div className="p-4 rounded-xl bg-[#141E34]/80 border border-slate-800">
                  <span className="text-xs text-slate-400 block mb-1">Average Rubric Score</span>
                  <div className="flex items-baseline gap-1">
                    <span className="text-2xl font-extrabold text-white">{stats.average_score}</span>
                    <span className="text-xs text-slate-400 font-medium">/ 100</span>
                  </div>
                  <div className="flex items-center gap-1 text-xs text-emerald-400 font-medium mt-1">
                    <TrendingUp className="w-3.5 h-3.5" />
                    <span>{stats.score_detail}</span>
                  </div>
                </div>

              </div>

              {/* DUAL INGESTION DROPZONE INTERACTIVE ACTION */}
              <div className="p-6 sm:p-8 text-center bg-[#0B0F19]">
                <div className="max-w-md mx-auto p-6 rounded-2xl border-2 border-dashed border-slate-800 bg-[#0F1626]/40 hover:border-brand-500/50 transition-colors">
                  <div className="w-12 h-12 rounded-full bg-brand-500/10 border border-brand-500/20 text-brand-400 flex items-center justify-center mx-auto mb-3">
                    <Upload className="w-6 h-6" />
                  </div>
                  <h3 className="text-sm sm:text-base font-bold text-white mb-1">
                    Dual Document Ingestion Engine
                  </h3>
                  <p className="text-xs text-slate-400 mb-4">
                    Upload agency call guidelines and proposal PDF for automated pre-flight audit.
                  </p>
                  
                  <button
                    onClick={handleEnterWorkspace}
                    className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-brand-500 hover:bg-brand-400 text-slate-950 font-bold text-xs uppercase tracking-wider cursor-pointer transition-all shadow-md shadow-brand-500/20"
                  >
                    <span>Launch Audit Workspace</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>

            </div>
          </section>
        </>
      )}

      {/* ACADEMIC FOOTER */}
      <footer id="about" className="mt-auto border-t border-slate-800/80 bg-[#070A12] py-8 text-center text-xs text-slate-400">
        <div className="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span className="font-bold text-white">GrantLens</span>
            <span>— AI Grant Auditing & Evaluation Platform (Week 2 Milestone)</span>
          </div>
          <p className="text-slate-400">
            Powered by FastAPI, SQLAlchemy 2.0, PostgreSQL 16, PyMuPDF & pdfplumber.
          </p>
        </div>
      </footer>

    </div>
  );
}

export default App;
