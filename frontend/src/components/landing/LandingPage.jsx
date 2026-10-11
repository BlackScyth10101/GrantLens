import React, { useState } from 'react';
import { Navbar } from './Navbar';
import { Hero } from './Hero';
import { AuditPreview } from './AuditPreview';
import { ProblemSolution } from './ProblemSolution';
import { FeaturesGrid } from './FeaturesGrid';
import { HowItWorks } from './HowItWorks';
import { FlagShowcase } from './FlagShowcase';
import { Footer } from './Footer';

export const LandingPage = () => {
  const [currentPersona, setCurrentPersona] = useState('researcher');

  const handleLaunchAudit = () => {
    // Smoothly scroll down to the audit workspace preview
    const workspaceElement = document.getElementById('audit-workspace');
    if (workspaceElement) {
      workspaceElement.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-navy-950 text-slate-100 flex flex-col selection:bg-brand-500 selection:text-white">
      {/* Navigation Header */}
      <Navbar
        currentPersona={currentPersona}
        onPersonaChange={setCurrentPersona}
        onLaunchAudit={handleLaunchAudit}
      />

      {/* Main Content Area */}
      <main className="flex-1">
        {/* 1. Hero Section */}
        <Hero
          currentPersona={currentPersona}
          onCtaClick={handleLaunchAudit}
        />

        {/* 2. Interactive Audit Workspace Preview Mockup (Matching User Reference) */}
        <AuditPreview />

        {/* 3. Problem vs. Solution Comparison */}
        <ProblemSolution />

        {/* 4. Core Features Grid (6 High-Density Cards) */}
        <FeaturesGrid />

        {/* 5. How It Works (3-Step Pipeline) */}
        <HowItWorks />

        {/* 6. Color-Coded Flag Showcase & AI Rewrite Diff */}
        <FlagShowcase />
      </main>

      {/* 7. Academic Footer & Disclaimers */}
      <Footer />
    </div>
  );
};
