from django.contrib import admin
from django.utils.html import format_html
from .models import LeaveRequest

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = [
        'user',
        'leave_type',
        'start_date',
        'end_date',
        'status',
        'submitted_at',
        'approved_by',
        'is_pending',  # <-- Added Pending indicator
    ]
    
    # Filters on the right sidebar
    list_filter = ['status', 'leave_type', 'start_date', 'end_date']
    
    # Add search functionality
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'reason']
    
    # Default ordering of records
    ordering = ['-submitted_at']

    # Make certain fields read-only
    readonly_fields = ['submitted_at']
    
    # Optional: group fields in the admin form for clarity
    fieldsets = (
        ('Leave Details', {
            'fields': ('user', 'leave_type', 'start_date', 'end_date', 'reason')
        }),
        ('Approval', {
            'fields': ('status', 'approved_by', 'submitted_at')
        }),
    )

    # Custom column to highlight pending requests
    def is_pending(self, obj):
        if obj.status == 'Pending':
            return format_html('<span style="color: red; font-weight: bold;">Pending</span>')
        return '—'
    
    is_pending.short_description = 'Pending Status'

