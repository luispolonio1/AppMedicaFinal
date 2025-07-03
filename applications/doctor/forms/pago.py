import re
from django import forms
from django.forms import ModelForm
from django.utils import timezone

from applications.doctor.models import Pago          # ajusta el import a tu app real
from applications.doctor.models import Atencion      # si lo necesitas en un <select>

class PagoForm(ModelForm):
    class Meta:
        model = Pago
        fields = [
            "atencion",
            "metodo_pago",
            "monto_total",
            "estado",
            "fecha_pago",
            "nombre_pagador",
            "referencia_externa",
            "evidencia_pago",
            "observaciones",
            "activo",
        ]
        widgets = {
            # -------- Relaciones --------
            "atencion": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            # -------- ChoiceFields --------
            "metodo_pago": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "estado": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            # -------- Básicos --------
            "monto_total": forms.NumberInput(attrs={
                "step": "0.01",
                "placeholder": "0.00",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "fecha_pago": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "nombre_pagador": forms.TextInput(attrs={
                "placeholder": "Nombre de la persona que paga",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "referencia_externa": forms.TextInput(attrs={
                "placeholder": "Nº transacción PayPal, etc.",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "observaciones": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Notas adicionales…",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 \
rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "rounded-md border-gray-300 text-blue-600 focus:ring-blue-500",
            }),
        }
        labels = {
            "atencion": "Atención relacionada",
            "metodo_pago": "Método de pago",
            "monto_total": "Monto total",
            "estado": "Estado",
            "fecha_pago": "Fecha de pago",
            "nombre_pagador": "Nombre del pagador",
            "referencia_externa": "Referencia externa",
            "evidencia_pago": "Comprobante / evidencia",
            "observaciones": "Observaciones",
            "activo": "Activo",
        }

    # Ejemplo de limpieza extra si quisieras validar referencia_externa:
    def clean_referencia_externa(self):
        ref = self.cleaned_data.get("referencia_externa")
        if self.cleaned_data.get("metodo_pago") != "efectivo" and not ref:
            raise forms.ValidationError("Se requiere una referencia para pagos digitales.")
        return ref
