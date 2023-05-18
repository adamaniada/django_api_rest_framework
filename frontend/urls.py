from django.urls import path, include
from .views import (
    api_v1_documentation
)

urlpatterns = [
    path('profile/', api_v1_documentation, name="api_v1_documentation"),
]
