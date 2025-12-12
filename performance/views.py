# performance/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PerformanceReview
from .serializers import PerformanceReviewSerializer

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            return PerformanceReview.objects.filter(status='Pending')
        elif user.is_ceo:
            return PerformanceReview.objects.filter(status='RegionalApproved')
        else:
            return PerformanceReview.objects.filter(user=user)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        review = self.get_object()
        user = request.user
        if user.is_manager and review.status == 'Pending':
            review.status = 'RegionalApproved'
        elif user.is_ceo and review.status == 'RegionalApproved':
            review.status = 'HeadOfficeApproved'
        else:
            return Response({"error": "Cannot approve"}, status=403)
        review.approved_by = user
        review.save()
        return Response({"status": review.status})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        review = self.get_object()
        review.status = 'Rejected'
        review.approved_by = request.user
        review.save()
        return Response({"status": review.status})


