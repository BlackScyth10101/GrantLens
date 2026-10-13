# syntax=docker/dockerfile:1.4
FROM python:3.11-slim-bookworm AS base

# Prevent Python from writing .pyc files and enable unbuffered standard IO
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

# Install native OS dependencies for PyMuPDF, pdfplumber, cryptography, and PostgreSQL client
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    libpq-dev \
    libmupdf-dev \
    mupdf-tools \
    libfreetype6-dev \
    libharfbuzz-dev \
    libjbig2dec0-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    zlib1g-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Stage dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r /app/requirements.txt

# Create application data and upload cache directories
RUN mkdir -p /app/storage/uploads /app/storage/reports

# Copy source tree
COPY . /app

# Create non-privileged service user for runtime isolation
RUN groupadd -g 10001 grantlens && \
    useradd -u 10000 -g grantlens -s /bin/bash -m grantlens && \
    chown -R grantlens:grantlens /app/storage

USER grantlens

EXPOSE 8000

HEALTHCHECK --interval=15s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/api/v1/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
