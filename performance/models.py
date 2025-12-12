from django.db import models
from django.conf import settings

class PerformanceReview(models.Model):
    REVIEW_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('RegionalApproved', 'Regional Approved'),
        ('HeadOfficeApproved', 'Head Office Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    remarks = models.TextField()
    review_date = models.DateField()
    status = models.CharField(max_length=20, choices=REVIEW_STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='review_approver',
        null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.user.username} - {self.status}"

