"""
=============================================================================
GrantLens Backend - Master Configuration Settings (settings.py)
=============================================================================
Project: GrantLens - AI Grant Auditing & Evaluation Platform
Scope: Week 1 Milestone - Core Configuration, CORS Middleware, & DRF Setup

Purpose:
This file contains the configuration for the Django project. It controls
installed applications, middleware pipelines, database connections, and
security settings (specifically Cross-Origin Resource Sharing).
=============================================================================
"""

from pathlib import Path

# BASE_DIR: The root filesystem directory of the Django project backend.
# Points to d:\GrantLens\backend. Used to resolve local database paths.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Secret key used for cryptographic signing in production.
# In production, this should be loaded from an environment variable (.env).
SECRET_KEY = 'django-insecure-j$we_h^3i%xgr^_h0!p404442m@*lshp70&+klb)3^$!l)hvo0'

# DEBUG MODE: Set to True for development to display detailed error tracebacks.
# Must be set to False in a production deployment.
DEBUG = True

# ALLOWED_HOSTS: List of host/domain names that this Django site can serve.
# '*' allows all local hostnames (127.0.0.1, localhost) during local development.
ALLOWED_HOSTS = ['*']


# =============================================================================
# APPLICATION DEFINITION (INSTALLED_APPS)
# =============================================================================
# Tells Django which modules and third-party libraries are active.
INSTALLED_APPS = [
    # Core Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Libraries:
    # 1. corsheaders: Enables Cross-Origin Resource Sharing so our React
    #    client on port 5173 can communicate with Django on port 8000.
    'corsheaders',

    # 2. rest_framework: Enables Django REST Framework (DRF) for API serialization,
    #    request parsers, and standardized JSON responses.
    'rest_framework',
]


# =============================================================================
# MIDDLEWARE PIPELINE (MIDDLEWARE)
# =============================================================================
# Django processes middleware in an "Onion" architecture:
# - Incoming requests execute middleware from top to bottom (index 0 -> n).
# - Outgoing responses execute middleware from bottom to top (index n -> 0).
#
# ⚠️ CRITICAL CS CONCEPT:
# 'corsheaders.middleware.CorsMiddleware' MUST be placed at index 0 (the very top).
# When the browser sends a preflight HTTP OPTIONS request, CorsMiddleware must
# intercept it immediately and attach the 'Access-Control-Allow-Origin' header
# before any other middleware (like CSRF or Authentication) can reject the request.
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Index 0: Intercepts CORS preflights first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Specifies the Python module that contains the root URL routing table.
ROOT_URLCONF = 'grantlens_backend.urls'

# Template engine configuration (used if rendering server-side HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# The Python entry point for WSGI-compliant web servers (Gunicorn, uWSGI)
WSGI_APPLICATION = 'grantlens_backend.wsgi.application'


# =============================================================================
# DATABASE CONFIGURATION (DATABASES)
# =============================================================================
# Week 1 uses SQLite (db.sqlite3) for lightweight local setup.
# In Week 2, this will be configured to connect to PostgreSQL for production
# compliance rulesets and vector store metadata.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Disabled password validation rules during early development
AUTH_PASSWORD_VALIDATORS = []


# =============================================================================
# INTERNATIONALIZATION & LOCALIZATION
# =============================================================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static assets URL routing
STATIC_URL = 'static/'


# =============================================================================
# CROSS-ORIGIN RESOURCE SHARING (CORS) SETTINGS
# =============================================================================
# By default, modern web browsers enforce the Same-Origin Policy (SOP).
# Since our React frontend is on http://localhost:5173 and Django is on
# http://127.0.0.1:8000, they have different origins.
#
# Setting CORS_ALLOW_ALL_ORIGINS = True instructs Django to attach
# 'Access-Control-Allow-Origin: *' to every HTTP response, giving the browser
# permission to deliver the JSON data to our React application.
CORS_ALLOW_ALL_ORIGINS = True

# Allows client requests to include HTTP cookies or credentials if needed later.
CORS_ALLOW_CREDENTIALS = True
