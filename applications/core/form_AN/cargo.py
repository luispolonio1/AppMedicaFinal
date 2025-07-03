from django import forms
from django.forms import ModelForm

from applications.core.models import Cargo


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = [
            "nombre",
            "descripcion",
            "activo",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej.: Médico, Enfermero…",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Descripción breve del rol…",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-checkbox h-5 w-5 text-blue-600",
            }),
        }
        labels = {
            "nombre": "Nombre del cargo",
            "descripcion": "Descripción",
            "activo": "Activo",
        }
        error_messages = {
            "nombre": {
                "unique": "Ya existe un cargo con este nombre.",
            },
        }

    # Normalizar nombre (quitar espacios extremos y capitalizar)
    def clean_nombre(self):
        return self.cleaned_data["nombre"].strip().title()
