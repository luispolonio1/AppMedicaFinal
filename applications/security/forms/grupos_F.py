import re
from django import forms
from django.forms import ModelForm
from applications.security.models import Group

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = [
            "name",
            "permissions",
        ]
        error_messages = {
            "name": {
                "unique": "Ya existe un grupo con este nombre.",
            },
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }),
            "permissions": forms.SelectMultiple(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }),
        }