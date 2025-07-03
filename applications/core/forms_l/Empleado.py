from django import forms
from django.forms import ModelForm
from applications.core.models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres', 'apellidos','cedula_ecuatoriana','dni','fecha_nacimiento','cargo','sueldo','fecha_ingreso','direccion','latitud','longitud','foto','activo']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula_ecuatoriana': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nombres': 'Nombre',
            'apellidos': 'Apellido',
            'cedula_ecuatoriana': 'Cédula Ecuatoriana',
            'dni': 'DNI',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'cargo': 'Cargo',
            'sueldo': 'Sueldo',
            'fecha_ingreso': 'Fecha de Ingreso',
            'direccion': 'Dirección',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'foto': 'Foto',
            'activo': 'Activo'
        }