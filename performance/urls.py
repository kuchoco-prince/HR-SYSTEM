from django.urls import path
from . import views   # ← THIS LINE FIXES THE ERROR

urlpatterns = [
    path('', views.performance_list, name='performance_list'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
]
