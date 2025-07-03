from django import forms
from django.forms import ModelForm
from applications.core.models import TipoGasto

class TipoGastoForm(ModelForm):
    class Meta:
        model = TipoGasto
        fields = [
            "nombre",
            "descripcion",
            "activo",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej.: Arriendo",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Detalle adicional del gasto...",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                         "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-checkbox h-5 w-5 text-blue-600",
            }),
        }
        labels = {
            "nombre": "Nombre del Tipo de Gasto",
            "descripcion": "Descripción del Gasto",
            "activo": "Activo",
        }
        error_messages = {
            "nombre": {
                "unique": "Ya existe un tipo de gasto con este nombre.",
            },
        }

    def clean_nombre(self):
        return self.cleaned_data["nombre"].strip().title()
