from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'role', 'department', 'supervisor']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show eligible supervisors
        self.fields['supervisor'].queryset = User.objects.filter(role__in=[
            'DistrictCoordinator', 'BAC/BRCHead', 'RegionalManager', 'Director', 'CEO'
        ])
