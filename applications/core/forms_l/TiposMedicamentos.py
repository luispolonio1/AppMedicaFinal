from django import forms
from django.forms import ModelForm
from applications.core.models import TipoMedicamento

class TipoMedicamentoForm(ModelForm):
    class Meta:
        model = TipoMedicamento
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del tipo de medicamento'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del tipo de medicamento'}),
        }
        labels = {
            'nombre': 'Tipo de Medicamento',
            'descripcion': 'Descripción',
        }