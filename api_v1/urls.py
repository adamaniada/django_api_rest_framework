from django.urls import path, include
from .views import (
    TransactionListApiView,
    TransactionDetailApiView,
    api_v1_documentation
)

urlpatterns = [
    path('exchange/', TransactionListApiView.as_view()),
    path('exchange/<int:todo_id>/', TransactionDetailApiView.as_view()),
    path('docs/', api_v1_documentation, name="api_v1_documentation"),
]
