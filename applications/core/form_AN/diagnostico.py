from django import forms
from django.forms import ModelForm

from applications.core.models import Diagnostico


class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = [
            "codigo",
            "descripcion",
            "datos_adicionales",
            "activo",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={
                "placeholder": "Ej.: A09",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "descripcion": forms.TextInput(attrs={
                "placeholder": "Gastroenteritis viral",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "datos_adicionales": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Notas u observaciones clínicas…",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-checkbox h-5 w-5 text-blue-600",
            }),
        }
        labels = {
            "codigo": "Código",
            "descripcion": "Descripción",
            "datos_adicionales": "Datos adicionales",
            "activo": "Activo",
        }
        error_messages = {
            "codigo": {
                "unique": "Ya existe un diagnóstico con este código.",
            },
        }

    # Normalizar el código (mayúsculas, sin espacios)
    def clean_codigo(self):
        return self.cleaned_data["codigo"].strip().upper()
