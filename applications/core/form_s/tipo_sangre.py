from django import forms
from django.forms import ModelForm
from applications.core.models import TipoSangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ['tipo', 'descripcion']
        widgets = {
            'tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el tipo de sangre (ej. A+, O-)',
            }),
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción opcional del tipo de sangre',
            }),
        }
        labels = {
            'tipo': 'Tipo de Sangre',
            'descripcion': 'Descripción',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].required = True
        self.fields['descripcion'].required = False
