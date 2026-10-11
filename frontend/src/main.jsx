/**
 * =============================================================================
 * GrantLens Frontend - Application Bootstrap Entrypoint (src/main.jsx)
 * =============================================================================
 * Project: GrantLens - AI Grant Auditing & Evaluation Platform
 * Scope: Week 1 Milestone - React 18 Concurrent Root Mounting & Global CSS Import
 * 
 * Execution Flow:
 * 1. The browser parses index.html and encounters <script type="module" src="/src/main.jsx">.
 * 2. main.jsx imports React runtime, global Tailwind stylesheet (index.css), and App.jsx.
 * 3. createRoot() attaches to the empty <div id="root"> element in index.html.
 * 4. React mounts the Virtual DOM and performs the initial paint of <App />.
 * =============================================================================
 */

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';     // Imports global Tailwind styles & resets
import App from './App.jsx'; // Imports the root component

// createRoot(): React 18+ API enabling Concurrent Rendering and automatic batching.
// document.getElementById('root'): Queries the single HTML mount container.
createRoot(document.getElementById('root')).render(
  // StrictMode: Development wrapper that checks for unsafe lifecycles,
  // legacy API usage, and unintentional side effects (runs effects twice in dev).
  <StrictMode>
    <App />
  </StrictMode>,
);
