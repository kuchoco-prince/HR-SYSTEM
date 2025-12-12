from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    role = request.user.role

    if role == "CEO":
        template = "dashboards/CEO_dashboard.html"
    elif role == "Director":
        template = "dashboards/Director_dashboard.html"
    elif role == "RegionalManager":
        template = "dashboards/Regional_dashboard.html"
    elif role == "DistrictCoordinator":
        template = "dashboards/District_dashboard.html"
    elif role == "BAC/BRCHead":
        template = "dashboards/BAC_dashboard.html"
    else:
        template = "dashboards/default_dashboard.html"

    return render(request, template)
