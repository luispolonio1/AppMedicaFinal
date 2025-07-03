from django import forms
from django.forms import ModelForm
from applications.doctor.models import HorarioAtencion


class HorarioAtencionForm(ModelForm):
    class Meta:
        model = HorarioAtencion
        fields = [
            "dia_semana",
            "hora_inicio",
            "hora_fin",
            "intervalo_desde",
            "intervalo_hasta",
            "activo",
        ]
        widgets = {
            "dia_semana": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
            "hora_inicio": forms.TimeInput(attrs={
                "type": "time",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
            "hora_fin": forms.TimeInput(attrs={
                "type": "time",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
            "intervalo_desde": forms.TimeInput(attrs={
                "type": "time",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
            "intervalo_hasta": forms.TimeInput(attrs={
                "type": "time",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5"
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-checkbox h-5 w-5 text-blue-600"
            }),
        }
        labels = {
            "dia_semana": "Día de la Semana",
            "hora_inicio": "Hora de Inicio",
            "hora_fin": "Hora de Fin",
            "intervalo_desde": "Intervalo Desde",
            "intervalo_hasta": "Intervalo Hasta",
            "activo": "Activo",
        }
