"""
================================================================================
GrantLens Compliance & Audit Engine - Primary Application Gateway (main.py)
================================================================================
Project: GrantLens (CSE299 Section 3, Group 3)
Milestone: Week 3 - Gemini AI API Integration & Full-Stack Portal
Author: Hasin Anzum Inan, Anas Ibne Majbha, Tazreen Alam, Israt Jahan Susmi
================================================================================
Entrypoint for the GrantLens FastAPI asynchronous web server:
- Lifespan Context Manager: Automatically initializes relational tables (users,
  submissions, documents, audits, budget items, and ai_reviews) on boot.
- CORS Security Middleware: Authorizes cross-origin requests from the React + Vite
  frontend development server (http://localhost:5173 / http://127.0.0.1:5173).
- REST Router Aggregation: Mounts the primary `/api/v1` router containing
  researcher auth, PyMuPDF dual-document ingestion, and Google Gemini AI audit routes.
- Legacy Telemetry Fallback: Preserves backwards compatibility for Week 1 metrics.
================================================================================
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import router as api_v1_router, platform_telemetry


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Asynchronous lifespan context manager:
    Executes table creation (DDL) before incoming requests are accepted,
    ensuring all relational models and foreign key constraints exist.
    """
    await init_db()
    yield


# Initialize FastAPI application instance with rich metadata for OpenAPI docs
app = FastAPI(
    title="GrantLens Dual-Engine Compliance & AI Audit Platform",
    description=(
        "Automated Pre-Flight Grant Audit Engine combining PyMuPDF formatting verification "
        "and Google Gemini 1.5 Flash narrative peer-review analysis for academic researchers."
    ),
    version="3.0.0",
    lifespan=lifespan,
)

# ------------------------------------------------------------------------------
# Cross-Origin Resource Sharing (CORS) Middleware Configuration
# ------------------------------------------------------------------------------
# Permits secure communication between React frontend and FastAPI backend across
# local loopback variations (localhost, 127.0.0.1, IPv4/IPv6 loopbacks).
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:[0-9]+)?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount primary `/api/v1` router containing auth, ingestion, and Gemini AI routes
app.include_router(api_v1_router)


# ------------------------------------------------------------------------------
# Backward Compatibility & Status Route (Week 1 & 2 Health Checks)
# ------------------------------------------------------------------------------
@app.get("/api/status/")
@app.get("/api/status")
async def legacy_status():
    """
    Maintains backward compatibility with Week 1 frontend status requests.
    """
    from database import AsyncSessionLocal
    async with AsyncSessionLocal() as session:
        return await platform_telemetry(db=session)


@app.get("/api/v1/health")
@app.get("/")
async def healthcheck():
    """
    Lightweight health check probe for load balancers and container orchestrators.
    """
    return {
        "status": "online",
        "service": "GrantLens Dual-Engine FastAudit Core",
        "version": "3.0.0",
        "ai_engine": "Google Gemini 1.5 Flash",
    }


if __name__ == "__main__":
    import uvicorn
    # Bind to 0.0.0.0:8000 to accept connections from both local host and containers
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
