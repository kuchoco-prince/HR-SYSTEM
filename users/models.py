# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Employee', 'Employee'),
        ('DistrictCoordinator', 'District Coordinator'),
        ('BAC/BRCHead', 'BAC/BRC Head'),
        ('RegionalManager', 'Regional Manager'),
        ('Director', 'Director'),
        ('CEO', 'CEO'),
        ('HR', 'HR Director'),
    ]
    
    department = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='Employee')
    supervisor = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='subordinates'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
