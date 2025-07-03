from django import forms
from django.forms import ModelForm
from applications.core.models import GastoMensual



class GastoMensualForm(ModelForm):
    class Meta:
        model = GastoMensual
        fields = ['tipo_gasto', 'fecha', 'valor', 'observacion']
        widgets = {
            'tipo_gasto': forms.Select(attrs={
                'class': 'form-control', 
            }),
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ingrese el valor del gasto'
            }),
            'observacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Comentario adicional (opcional)'
            }),
        }
