# citas/forms.py
from django import forms
from applications.doctor.models import CitaMedica
from datetime import time

class CitaMedicaForm(forms.ModelForm):
    HORA_OPCIONES = [
        (time(h, 0), f"{h:02d}:00")
        for h in range(6, 19, 2) 
    ]

    hora_cita = forms.ChoiceField(
        choices=[('', 'Seleccione hora')] + [(h.strftime("%H:%M"), h.strftime("%H:%M")) for h, _ in HORA_OPCIONES],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = CitaMedica
        fields = ['hora_cita', 'observaciones']
