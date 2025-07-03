from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.doctor.models import DetallePago
from applications.doctor.forms.detalle_pago import DetallePagoForm


class DetallePagoListView(PermissionMixin, ListViewMixin, ListView):
    model = DetallePago
    template_name = "doctor/detalle_pagos/list.html"
    context_object_name = "detalles"
    permission_required = "view_detallepago"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(
                Q(servicio_adicional__nombre__icontains=q) |
                Q(descripcion_seguro__icontains=q),
                Q.OR
            )
        return DetallePago.objects.filter(self.query).order_by('-id')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("doctor:detallepago_create")
        return ctx


class DetallePagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = DetallePago
    form_class = DetallePagoForm
    template_name = "doctor/detalle_pagos/form.html"
    success_url = reverse_lazy("doctor:detallepago_list")
    permission_required = "add_detallepago"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Crear Detalle de Pago"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Detalle de pago creado correctamente.")
        self.object.actualizar_total_pago()
        return response


class DetallePagoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = DetallePago
    form_class = DetallePagoForm
    template_name = "doctor/detalle_pagos/form.html"
    success_url = reverse_lazy("doctor:detallepago_list")
    permission_required = "change_detallepago"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Detalle de Pago"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Detalle de pago actualizado correctamente.")
        self.object.actualizar_total_pago()
        return response


class DetallePagoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = DetallePago
    template_name = "core/delete.html"
    success_url = reverse_lazy("doctor:detallepago_list")
    permission_required = "delete_detallepago"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Detalle de Pago"
        ctx["description"] = f"¿Desea eliminar este detalle: {self.object.servicio_adicional}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        pago = self.object.pago
        response = super().form_valid(form)
        pago.detalles.first().actualizar_total_pago() if pago.detalles.exists() else pago.save()
        messages.success(self.request, "Detalle de pago eliminado correctamente.")
        return response
