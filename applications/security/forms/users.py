# forms/user.py

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'is_active', 'is_staff', 'is_superuser', 'groups'
        ]
        error_messages = {
            'username': {
                'unique': 'Ya existe un usuario con este nombre de usuario.',
            },
            'email': {
                'unique': 'Ya existe un usuario con este correo electrónico.',
            },
        }
        widgets = {
            'groups': forms.CheckboxSelectMultiple()
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username.lower()
        

