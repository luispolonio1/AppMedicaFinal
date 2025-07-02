from django import forms
from django.forms import ModelForm
from applications.doctor.models import CitaMedica

class CitaMedicaForm(ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['paciente', 'fecha', 'hora_cita', 'estado']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_cita': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),  # ✅ también aquí usa el nombre correcto
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'paciente': 'Paciente',
            'fecha': 'Fecha de la cita',
            'hora_cita': 'Hora de la cita',
            'estado': 'Estado de la cita',
            'observaciones': 'Observaciones',
        }
