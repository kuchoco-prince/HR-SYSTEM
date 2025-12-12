from django.shortcuts import render, redirect
from .models import PerformanceReview
from django.contrib.auth.decorators import login_required

@login_required
def performance_index(request):
    reviews = PerformanceReview.objects.filter(user=request.user)
    return render(request, "performance/index.html", {"reviews": reviews})


@login_required
def performance_form(request):
    if request.method == "POST":
        PerformanceReview.objects.create(
            user=request.user,
            score=request.POST.get("score"),
            comments=request.POST.get("comments"),
            status="Pending"
        )
        return redirect("performance-index")

    return render(request, "performance/performance_form.html")
