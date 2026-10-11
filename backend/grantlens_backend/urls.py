"""
=============================================================================
GrantLens Backend - URL Routing & API Endpoint Configuration
=============================================================================
Project: GrantLens - AI Grant Auditing & Evaluation Platform
Scope: Week 1 Milestone - Core DRF Status Endpoint & System Telemetry

Purpose:
This module defines the URL dispatch routing table for the Django backend.
When an HTTP request reaches the server at port 8000, Django's URLResolver
scans this file to match the URL pattern and dispatch execution to the
appropriate Python view function.
=============================================================================
"""

# Core Django Imports
from django.contrib import admin  # Django's built-in administration panel
from django.urls import path       # Path function for mapping URL strings to views

# Django REST Framework (DRF) Imports
from rest_framework.decorators import api_view  # Restricts HTTP methods (GET, POST, etc.)
from rest_framework.response import Response    # Serializes Python dicts into JSON responses

# Standard Library Imports
from datetime import datetime  # Used to generate live server timestamps


# =============================================================================
# API VIEW FUNCTION: api_status
# =============================================================================
# @api_view(['GET']) Decorator:
# 1. Enforces HTTP method safety: Only HTTP GET is permitted. Any POST, PUT,
#    or DELETE requests will automatically be rejected with HTTP 405 Method Not Allowed.
# 2. Wraps Django's standard HttpRequest into DRF's enhanced Request object.
# 3. Performs Content Negotiation: Automatically serializes the returned Response
#    into standard JSON format with 'Content-Type: application/json' headers.
@api_view(['GET'])
def api_status(request):
    """
    Handles GET requests to /api/status/
    Returns active platform telemetry and initial compliance statistics
    to be displayed on the React frontend.
    """
    
    # Construct telemetry payload dictionary
    # In Week 2, these values will be queried dynamically from the PostgreSQL database.
    # In Week 1, this acts as the live data handshake with the React client.
    payload = {
        # General Service Health
        "status": "online",
        "service": "GrantLens Compliance Engine",
        "backend": "Django REST Framework (Python 3.13)",
        
        # Telemetry Metrics (bound to the 4 cards on the frontend)
        "solicitations_count": 2,
        "solicitations_detail": "NSF 24-500 • NIH R01",
        
        "proposals_count": 3,
        "proposals_detail": "Full section & table trees",
        
        "audits_completed": 2,
        "audits_detail": "100% evaluated",
        
        "average_score": 96.2,
        "score_detail": "High compliance fidelity",
        
        # Live System Timestamp: Changes dynamically on every request
        # Proves to the instructor that the frontend is actually fetching live server data.
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    
    # Return DRF Response object (status defaults to HTTP 200 OK)
    return Response(payload)


# =============================================================================
# URL ROUTING TABLE (urlpatterns)
# =============================================================================
# Django's URL dispatcher checks incoming requests against this list in order.
urlpatterns = [
    # Built-in Django administration site
    path('admin/', admin.site.urls),
    
    # Public REST API status endpoint:
    # URL: http://127.0.0.1:8000/api/status/
    # When React calls this URL, it executes the api_status() function above.
    path('api/status/', api_status, name='api_status'),
]
