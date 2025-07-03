from django import forms
from django.forms import ModelForm
from applications.core.models import FotoPaciente

class FotoPacienteForm(ModelForm):
    class Meta:
        model = FotoPaciente
        fields = ["paciente", "imagen", "descripcion"]
        widgets = {
            "paciente": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
            "imagen": forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50",
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Ej. Imagen postoperatoria de cicatriz...",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
        }
        labels = {
            "paciente": "Paciente",
            "imagen": "Imagen",
            "descripcion": "Descripción",
        }
