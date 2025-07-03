from django import forms
from django.forms import ModelForm
from applications.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields = ['nombres', 'apellidos', 'ruc', 'fecha_nacimiento', 
                'direccion','latitud','longitud','codigo_unico_doctor',
                'especialidad','telefonos','email','horario_atencion','duracion_atencion',
                'curriculum','firma_digital','foto','imagen_receta','activo']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los nombres del doctor'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los apellidos del doctor'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el RUC del doctor'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección del doctor'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la latitud'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la longitud'}),
            'codigo_unico_doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el código único del doctor'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la especialidad del doctor'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono del doctor'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el email del doctor'}),
            'horario_atencion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el horario de atención'}),
            'duracion_atencion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la duración de atención en minutos'}),
            'curriculum': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'firma_digital': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'imagen_receta': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }