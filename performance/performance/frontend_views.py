# frontend_views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from performance.models import PerformanceReview  # Absolute import, Pylance-safe

# Example view: list all performance reviews
@login_required
def performance_list(request):
    reviews = PerformanceReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'performance/performance_list.html', context)

# Example view: detail of a single review
@login_required
def performance_detail(request, review_id):
    review = get_object_or_404(PerformanceReview, id=review_id)
    context = {'review': review}
    return render(request, 'performance/performance_detail.html', context)

# Example API view: return JSON of all reviews
@login_required
@require_http_methods(["GET"])
def performance_list_api(request):
    reviews = PerformanceReview.objects.all().values('id', 'user_id', 'score', 'comments', 'created_at')
    return JsonResponse(list(reviews), safe=False)

