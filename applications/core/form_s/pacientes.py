from django import forms
from django.forms import ModelForm
from applications.core.models import Paciente

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombres',
            'apellidos',
            'cedula_ecuatoriana',
            'dni',
            'fecha_nacimiento',
            'telefono',
            'email',
            'sexo',
            'estado_civil',
            'direccion',
            'latitud',
            'longitud',
            'tipo_sangre',
            'foto',
            'antecedentes_personales',
            'antecedentes_quirurgicos',
            'antecedentes_familiares',
            'alergias',
            'medicamentos_actuales',
            'habitos_toxicos',
            'vacunas',
            'antecedentes_gineco_obstetricos',
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'foto': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'antecedentes_personales': forms.Textarea(attrs={'rows': 3}),
            'antecedentes_quirurgicos': forms.Textarea(attrs={'rows': 3}),
            'antecedentes_familiares': forms.Textarea(attrs={'rows': 3}),
            'alergias': forms.Textarea(attrs={'rows': 2}),
            'medicamentos_actuales': forms.Textarea(attrs={'rows': 3}),
            'vacunas': forms.Textarea(attrs={'rows': 2}),
            'antecedentes_gineco_obstetricos': forms.Textarea(attrs={'rows': 3}),
        }

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula_ecuatoriana': 'Cédula Ecuatoriana',
            'dni': 'Documento Internacional',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Teléfono(s)',
            'email': 'Correo Electrónico',
            'sexo': 'Sexo',
            'estado_civil': 'Estado Civil',
            'direccion': 'Dirección',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'tipo_sangre': 'Tipo de Sangre',
            'foto': 'Foto de Perfil',
            'antecedentes_personales': 'Antecedentes Personales Patológicos',
            'antecedentes_quirurgicos': 'Antecedentes Quirúrgicos',
            'antecedentes_familiares': 'Antecedentes Familiares',
            'alergias': 'Alergias',
            'medicamentos_actuales': 'Medicamentos Actuales',
            'habitos_toxicos': 'Hábitos Tóxicos o Perjudiciales',
            'vacunas': 'Vacunas',
            'antecedentes_gineco_obstetricos': 'Antecedentes Gineco-Obstétricos',
        }
