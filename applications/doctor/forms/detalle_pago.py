from decimal import Decimal
from django import forms
from django.forms import ModelForm

from applications.doctor.models import DetallePago

class DetallePagoForm(ModelForm):
    class Meta:
        model = DetallePago
        fields = [
            "pago",
            "servicio_adicional",
            "cantidad",
            "precio_unitario",
            "descuento_porcentaje",
            "aplica_seguro",
            "valor_seguro",
            "descripcion_seguro",
        ]
        widgets = {
            "pago": forms.Select(attrs={
                "class": "form-control",
            }),
            "servicio_adicional": forms.Select(attrs={
                "class": "form-control",
            }),
            "cantidad": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1,
            }),
            "precio_unitario": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),
            "descuento_porcentaje": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
                "min": 0,
                "max": 100,
            }),
            "aplica_seguro": forms.CheckboxInput(attrs={
                "class": "form-checkbox h-5 w-5 text-blue-600",
            }),
            "valor_seguro": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
            }),
            "descripcion_seguro": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Saludsa Nivel 2",
            }),
        }
        labels = {
            "pago": "Pago",
            "servicio_adicional": "Servicio Adicional",
            "cantidad": "Cantidad",
            "precio_unitario": "Precio Unitario",
            "descuento_porcentaje": "Descuento (%)",
            "aplica_seguro": "¿Aplica Seguro?",
            "valor_seguro": "Valor Seguro",
            "descripcion_seguro": "Descripción del Seguro",
        }
