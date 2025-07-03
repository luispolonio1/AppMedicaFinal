from django import forms
from applications.doctor.models import ServiciosAdicionales

class ServiciosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = [
            'nombre_servicio',
            'costo_servicio',
            'descripcion',
            'activo'
        ]
        widgets = {
            'nombre_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'costo_servicio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }