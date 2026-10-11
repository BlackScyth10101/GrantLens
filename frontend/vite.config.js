/**
 * =============================================================================
 * GrantLens Frontend - Vite Build Configuration (vite.config.js)
 * =============================================================================
 * Project: GrantLens - AI Grant Auditing & Evaluation Platform
 * Scope: Week 1 Milestone - Frontend Build Pipeline & Local Server Config
 * 
 * Why Vite over Create-React-App (CRA)?
 * 1. CRA uses Webpack, which bundles the entire application graph into memory
 *    before serving, causing slow cold starts (O(N) complexity).
 * 2. Vite leverages Browser-Native ES Modules (ESM) during development: files
 *    are requested on-demand over HTTP, while dependencies are pre-bundled
 *    using ESBuild (written in Go, which is 10-100x faster than Node bundlers).
 * 3. In production, Vite uses Rollup for tree-shaking and dead-code elimination,
 *    achieving sub-400ms production builds.
 * =============================================================================
 */

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath, URL } from 'node:url';

// https://vitejs.dev/config/
export default defineConfig({
  // 1. PLUGINS:
  // @vitejs/plugin-react enables Fast Refresh (HMR) and transforms JSX
  // syntax into native JavaScript function calls during build.
  plugins: [react()],

  // 2. PATH RESOLUTION ALIASES:
  // Maps the '@' prefix to the absolute path of './src'.
  // This avoids fragile relative import paths like '../../components/Header'
  // and allows clean imports like '@/components/Header'.
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },

  // 3. DEVELOPMENT SERVER OPTIONS:
  // Binds the local server to TCP Port 5173.
  // 'host: true' exposes the server to the local network for multi-device testing.
  server: {
    port: 5173,
    host: true,
  },
});
