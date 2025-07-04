from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.doctor.models import Pago
from applications.doctor.forms.pago import PagoForm

from applications.doctor.utils.PagosPaypal import generateAccessToken, createPago, capture_order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# ---------- LIST ----------
class PagoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = "doctor/pagos/list.html"
    model = Pago
    context_object_name = "pagos"
    permission_required = "view_pago"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            # Busca por id, nombre de pagador o referencia
            self.query.add(
                Q(id__exact=q) | Q(nombre_pagador__icontains=q) | Q(referencia_externa__icontains=q),
                Q.OR
            )
        return self.model.objects.filter(self.query).order_by("-fecha_creacion")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("doctor:pago_create")
        return ctx


# ---------- CREATE ----------
class PagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Pago
    form_class = PagoForm
    template_name = "doctor/pagos/form.html"
    success_url = reverse_lazy("doctor:pago_list")
    permission_required = "add_pago"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Registrar pago"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al registrar el pago #{self.object.id}.")
        print("Generating access token...")
        print(generateAccessToken())
        return response


# ---------- UPDATE ----------
class PagoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = "doctor/pagos/form.html"
    success_url = reverse_lazy("doctor:pago_list")
    permission_required = "change_pago"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar pago"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Pago #{self.object.id} actualizado correctamente.")
        return response


# ---------- DELETE ----------
class PagoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Pago
    template_name = "core/delete.html"          # ya la reutilizas
    success_url = reverse_lazy("doctor:pago_list")
    permission_required = "delete_pago"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar pago"
        ctx["description"] = f"¿Desea eliminar lógicamente el pago #{self.object.id}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        pago_id = self.object.id
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar lógicamente el pago #{pago_id}.")
        return response

@method_decorator(csrf_exempt, name='dispatch')
class PagoAPIView(APIView):
    def get(self, request):
        """Método GET para testing - muestra información sobre la API"""
        return Response({
            'message': 'PayPal API endpoint',
            'methods': ['POST'],
            'usage': 'Send POST request with JSON body containing "amount" field'
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            # Obtener los datos del request
            data = json.loads(request.body)
            amount = data.get('amount', 0)
            
            # Validar que el monto sea válido
            if not amount or amount <= 0:
                return Response({
                    'error': 'Amount must be greater than 0'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Crear la orden de pago
            order_data = createPago(amount)
            
            if order_data:
                return Response(order_data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error': 'Could not create order'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        except json.JSONDecodeError:
            return Response({
                'error': 'Invalid JSON data'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error creating order: {e}")
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(csrf_exempt, name='dispatch')
class CaptureOrderPAypal(APIView):
    def post(self, request, *args, **kwargs):
        try:
            order_id = self.kwargs['order_id']
            response = capture_order(order_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error capturing order: {e}")
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)