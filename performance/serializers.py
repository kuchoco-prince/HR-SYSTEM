# performance/serializers.py
from rest_framework import serializers
from .models import PerformanceReview

class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = '__all__'
        read_only_fields = ['status', 'submitted_at', 'approved_by']
