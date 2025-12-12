# ===============================
# DRF API VIEWS (Backend API)
# ===============================
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import Group
from .models import PerformanceReview
from .serializers import PerformanceReviewSerializer

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Performance Reviews.
    Managers see all reviews; regular users see only their own.
    """
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Check if user is in Manager group
        if user.groups.filter(name='Manager').exists():
            return PerformanceReview.objects.all()

        # Regular users see only their own reviews
        return PerformanceReview.objects.filter(user=user)

    @action(detail=False, methods=['get'])
    def my_reviews(self, request):
        """
        Endpoint to fetch the logged-in user's own performance reviews.
        """
        reviews = PerformanceReview.objects.filter(user=request.user)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)


# ===============================
# FRONTEND HTML VIEWS
# ===============================
from django.shortcuts import render, redirect
from .forms import PerformanceReviewForm

def performance_list(request):
    reviews = PerformanceReview.objects.filter(user=request.user)
    return render(request, 'performance/performance_list.html', {'reviews': reviews})

def upload_pdf(request):
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('performance_list')
    else:
        form = PerformanceReviewForm()
    return render(request, 'performance/upload_pdf.html', {'form': form})
