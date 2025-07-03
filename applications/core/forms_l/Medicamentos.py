from django import forms
from django.forms import ModelForm
from applications.core.models import Medicamento, TipoMedicamento

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['tipo','marca_medicamento', 'nombre', 'descripcion','concentracion',
                  'via_administracion','cantidad','precio','comercial','foto','activo']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'marca_medicamento': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'concentracion': forms.TextInput(attrs={'class': 'form-control'}),
            'via_administracion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'comercial': forms.CheckboxInput(),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'activo': forms.CheckboxInput(),
        }