from django import forms
from applications.doctor.models import DetalleAtencion

class DetalleAtencionForm(forms.ModelForm):
    class Meta:
        model = DetalleAtencion
        fields = [
            'atencion',
            'medicamento', 
            'cantidad',
            'prescripcion',
            'duracion_tratamiento',
            'frecuencia_diaria'
        ]
        widgets = {
            'atencion': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'medicamento': forms.Select(attrs={
                'class': 'form-control',
                'required': True
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'required': True,
                'placeholder': 'Ej: 10'
            }),
            'prescripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'required': True,
                'placeholder': 'Ej: Tomar 1 tableta cada 8 horas después de las comidas'
            }),
            'duracion_tratamiento': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Días de tratamiento'
            }),
            'frecuencia_diaria': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '24',
                'placeholder': 'Veces por día'
            })
        }
        labels = {
            'atencion': 'Atención Médica',
            'medicamento': 'Medicamento',
            'cantidad': 'Cantidad',
            'prescripcion': 'Prescripción',
            'duracion_tratamiento': 'Duración del Tratamiento (días)',
            'frecuencia_diaria': 'Frecuencia Diaria (veces por día)'
        }
        help_texts = {
            'atencion': 'Seleccione la atención médica asociada',
            'medicamento': 'Seleccione el medicamento a recetar',
            'cantidad': 'Número de unidades del medicamento',
            'prescripcion': 'Instrucciones detalladas para el paciente',
            'duracion_tratamiento': 'Opcional: Duración estimada del tratamiento',
            'frecuencia_diaria': 'Opcional: Cuántas veces al día tomar el medicamento'
        }