from django import forms
from django.forms import ModelForm
from applications.core.models import MarcaMedicamento

class MarcaMedicamentoForm(ModelForm):
    class Meta:
        model = MarcaMedicamento
        fields = ['nombre', 'descripcion','activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la marca'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la marca'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'activo': 'Activo',
        }