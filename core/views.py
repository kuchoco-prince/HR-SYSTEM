from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Check user's role
    role = getattr(request.user, 'role', None)  # Use getattr to avoid AttributeError

    if role == "CEO":
        template = "dashboard/CEO_dashboard.html"
    elif role == "Director":
        template = "dashboard/Director_dashboard.html"
    elif role == "RegionalManager":
        template = "dashboard/Regional_dashboard.html"
    elif role == "DistrictCoordinator":
        template = "dashboard/District_dashboard.html"
    elif role == "BAC/BRCHead":
        template = "dashboard/BAC_dashboard.html"
    else:
        template = "dashboard/user_dashboard.html"  # default dashboard

    return render(request, template)
