import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import router as api_v1_router, platform_telemetry


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize relational tables on startup
    await init_db()
    yield


app = FastAPI(
    title="GrantLens Compliance & Audit Engine",
    description="Automated Grant Audit & Ingestion Platform for Academic Research Offices",
    version="2.0.0",
    lifespan=lifespan,
)

# Cross-Origin Resource Sharing (CORS) Configuration
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

# Mount primary Week 2 API router
app.include_router(api_v1_router)

# Mount Week 1 legacy compatibility route for http://localhost:8000/api/status/
@app.get("/api/status/")
@app.get("/api/status")
async def legacy_status():
    from database import AsyncSessionLocal
    async with AsyncSessionLocal() as session:
        return await platform_telemetry(db=session)


@app.get("/api/v1/health")
@app.get("/")
async def healthcheck():
    return {
        "status": "online",
        "service": "GrantLens FastAudit Core",
        "version": "2.0.0",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
