
from django.urls import path
from .views import register_employee, login_user, logout_user

urlpatterns = [
    path('register/', register_employee, name='register_employee'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
