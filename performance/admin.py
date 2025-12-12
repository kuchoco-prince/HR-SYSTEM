from django.contrib import admin
from django.utils.html import format_html
from .models import PerformanceReview

@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = [
        'user',
        'remarks',
        'review_date',
        'status',
        'submitted_at',
        'approved_by',
        'pending_status',
        'appraisal_pdf',  # show file in admin
    ]

    # Filters on the right sidebar
    list_filter = ['status', 'review_date']

    # Search box
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'remarks']

    # Ordering
    ordering = ['-submitted_at']

    # Read-only fields
    readonly_fields = ['submitted_at']

    # Optional: group fields in the admin form
    fieldsets = (
        ('Review Details', {
            'fields': ('user', 'remarks', 'review_date', 'appraisal_pdf')  # added file
        }),
        ('Approval', {
            'fields': ('status', 'approved_by', 'submitted_at')
        }),
    )

    # Custom column to highlight pending reviews
    def pending_status(self, obj):
        if obj.status == 'Pending':
            return format_html('<span style="color: red; font-weight: bold;">Pending</span>')
        return '—'
    
    pending_status.short_description = 'Pending Approval'




  
