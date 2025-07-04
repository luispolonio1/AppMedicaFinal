import re
from django import forms
from django.forms import ModelForm
from applications.security.models import GroupModulePermission
from applications.security.models import Module
from django.contrib.auth.models import Permission

class GroupModulePermissionForm(ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = [
            "group",
            "module",
            "permissions",
        ]
        error_messages = {
            "group": {
                "unique_together": "Ya existe una relación con este grupo y módulo.",
            },
        }
        widgets = {
            "group": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }),
            "module": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }),
            "permissions": forms.SelectMultiple(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        module = None

        if 'module' in self.data:
            try:
                module_id = int(self.data.get('module'))
                module = Module.objects.get(pk=module_id)
            except (ValueError, TypeError, Module.DoesNotExist):
                pass
        elif self.instance.pk:
            module = self.instance.module

        if module:
            self.fields['permissions'].queryset = module.permissions.all()
            self.fields['permissions'].widget.attrs.pop('disabled', None)
        else:
            self.fields['permissions'].queryset = Permission.objects.none()
            self.fields['permissions'].widget.attrs['disabled'] = 'disabled'