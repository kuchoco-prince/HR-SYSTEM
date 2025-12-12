from django import forms
from .models import PerformanceReview

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['remarks', 'review_date', 'status', 'pdf_file']
