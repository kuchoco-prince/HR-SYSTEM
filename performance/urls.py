from django.urls import path
from .views import PerformanceReviewViewSet

urlpatterns = [
    path('reviews/', PerformanceReviewViewSet.as_view({'get':'list'}), name='performance-reviews'),
]
