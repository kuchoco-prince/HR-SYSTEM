from django.contrib import admin
from .models import PerformanceReview  # Only import performance models

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'submitted_at', 'approved_by']
    list_filter = ['status']
    search_fields = ['user__username']
