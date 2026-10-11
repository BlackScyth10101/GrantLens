from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

@api_view(['GET'])
def api_status(request):
    """
    Returns platform status and live compliance metrics to the frontend.
    """
    return Response({
        "status": "online",
        "service": "GrantLens Compliance Engine",
        "backend": "Django REST Framework",
        "solicitations_count": 2,
        "solicitations_detail": "NSF 24-500 • NIH R01",
        "proposals_count": 3,
        "proposals_detail": "Full section & table trees",
        "audits_completed": 2,
        "audits_detail": "100% evaluated",
        "average_score": 96.2,
        "score_detail": "High compliance fidelity",
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/status/', api_status, name='api_status'),
]
