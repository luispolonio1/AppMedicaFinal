from django import forms
from django.forms import ModelForm
from applications.doctor.models import CitaMedica
from django.utils import timezone

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
    def clean(self):
            cleaned_data = super().clean()
            fecha = cleaned_data.get('fecha')
            hora_cita = cleaned_data.get('hora_cita')

            if fecha and hora_cita:
                # Validar que no sea una fecha pasada
                if fecha < timezone.now().date():
                    raise forms.ValidationError({'fecha': 'No se pueden agendar citas en fechas pasadas'})
                
                # Validar que no exista cita duplicada (excepto para esta instancia si es una edición)
                if self.instance.pk:
                    if CitaMedica.objects.filter(fecha=fecha, hora_cita=hora_cita).exclude(pk=self.instance.pk).exists():
                        raise forms.ValidationError({'hora_cita': 'Este horario ya está ocupado'})
                else:
                    if CitaMedica.objects.filter(fecha=fecha, hora_cita=hora_cita).exists():
                        raise forms.ValidationError({'hora_cita': 'Este horario ya está ocupado'})

            return cleaned_data
