# leave/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer

# LeaveRequest API
class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

# Dashboard view (if dashboard is here)
def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Optional: requires login to view the dashboard
def dashboard_view(request):
    # You can pass context data here if needed
    context = {}
    return render(request, 'dashboard.html', context)

from django.shortcuts import render
def dashboard_view(request):
    return render(request, 'dashboard.html')

# leave/views.py
from django.shortcuts import render
def dashboard_view(request):
    return render(request, 'dashboard.html')
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
