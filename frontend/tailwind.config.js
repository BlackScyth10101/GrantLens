/**
 * =============================================================================
 * GrantLens Frontend - Tailwind CSS Design Configuration (tailwind.config.js)
 * =============================================================================
 * Project: GrantLens - AI Grant Auditing & Evaluation Platform
 * Scope: Week 1 Milestone - Design System, Theme Tokens & JIT Compilation
 * 
 * How Tailwind JIT (Just-In-Time) Works:
 * 1. The compiler inspects all files listed in the 'content' array.
 * 2. It parses every HTML/JSX token (e.g., 'bg-navy-950', 'text-brand-500').
 * 3. It generates ONLY the exact CSS classes used in our components, purging
 *    all unused styles. This produces an ultra-lean CSS output (32 KB).
 * =============================================================================
 */

/** @type {import('tailwindcss').Config} */
export default {
  // 1. CONTENT DISCOVERY GLOBS:
  // Tells Tailwind which files to scan for utility class names.
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],

  // Enables class-based dark mode (e.g., <html class="dark">)
  darkMode: 'class',

  theme: {
    extend: {
      // 2. CUSTOM COLOR TOKENS:
      // Defines the corporate visual identity of GrantLens.
      colors: {
        // Brand Color: High-visibility electric amber/orange
        brand: {
          50: '#FFF7ED',
          100: '#FFEDD5',
          200: '#FED7AA',
          300: '#FDBA74',
          400: '#FB923C',
          500: '#F97316', // Primary Accent used on buttons and highlights
          600: '#EA580C',
          700: '#C2410C',
          800: '#9A3412',
          900: '#7C2D12',
          glow: 'rgba(249, 115, 22, 0.4)',
        },

        // Navy & Obsidian Color Scale: Deep academic dark mode background
        navy: {
          950: '#070A12', // Base app background (#070A12)
          900: '#0B0F19', // Main container & card surface
          850: '#0F1626', // Elevated preview cards
          800: '#141E34', // Card backgrounds & metric tiles
          750: '#192642', // Card hover state
          700: '#1E2D4A', // Borders & rules
          600: '#2A3F66', // Highlight borders
          500: '#3D5A8A',
        },

        // Audit Severity Tokens: Used to color-code grant compliance violations
        severity: {
          fatal: '#EF4444',              // Red: Fatal desk-rejection infractions
          'fatal-bg': 'rgba(239, 68, 68, 0.12)',
          'fatal-border': 'rgba(239, 68, 68, 0.35)',
          warning: '#F59E0B',            // Amber: Budget discrepancies & warnings
          'warning-bg': 'rgba(245, 158, 11, 0.12)',
          'warning-border': 'rgba(245, 158, 11, 0.35)',
          success: '#10B981',            // Emerald: Compliant verified sections
          'success-bg': 'rgba(16, 185, 129, 0.12)',
          'success-border': 'rgba(16, 185, 129, 0.35)',
          info: '#38BDF8',               // Cyan: Informational guideline notes
          'info-bg': 'rgba(56, 189, 248, 0.12)',
          'info-border': 'rgba(56, 189, 248, 0.35)',
        }
      },

      // 3. TYPOGRAPHY FAMILIES:
      // Uses Inter for UI text and JetBrains Mono for audit rule codes.
      fontFamily: {
        sans: ['Inter', 'Plus Jakarta Sans', 'system-ui', 'sans-serif'],
        display: ['Plus Jakarta Sans', 'Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'Consolas', 'monospace'],
      },

      // 4. CUSTOM BOX SHADOWS:
      // Subtle glowing dropshadows for buttons and cards.
      boxShadow: {
        'glow-brand': '0 0 30px -5px rgba(249, 115, 22, 0.3)',
        'glow-brand-lg': '0 0 50px -10px rgba(249, 115, 22, 0.45)',
        'glow-fatal': '0 0 25px -5px rgba(239, 68, 68, 0.35)',
        'glow-success': '0 0 25px -5px rgba(16, 185, 129, 0.35)',
        'inner-glow': 'inset 0 1px 1px 0 rgba(255, 255, 255, 0.08)',
      },

      // 5. ANIMATIONS:
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-6px)' },
        }
      }
    },
  },

  plugins: [],
};
