from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.doctor.models import Pago
from applications.doctor.forms.pago import PagoForm


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
