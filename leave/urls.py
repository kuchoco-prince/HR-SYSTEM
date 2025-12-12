from django.urls import path
from .views import LeaveRequestViewSet

urlpatterns = [
    path('requests/', LeaveRequestViewSet.as_view({'get':'list'}), name='leave-requests'),
]
