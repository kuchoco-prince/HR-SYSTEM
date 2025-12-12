"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# core/urls.py
from django.contrib import admin
from django.urls import path, include
from leave.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('users/', include('users.urls')),

    # Leave App
    path('api/leave/', include('leave.urls')),

    # Performance App
    path('api/performance/', include('performance.urls')),

    # Dashboard
    path('dashboard/', dashboard_view, name='dashboard'),

    # Root → Dashboard
    path('', dashboard_view),
]
from django.contrib.auth import views as auth_views

urlpatterns += [
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),

    path('password-reset-sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_sent.html"),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),

    path('reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),
]
