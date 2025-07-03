from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.core.models import TipoGasto
from applications.core.form_AN.tipo_gasto import TipoGastoForm


class TipoGastoListView(PermissionMixin, ListViewMixin, ListView):
    model = TipoGasto
    template_name = "core_AN/tipo_gasto/list.html"
    context_object_name = "tipos_gasto"
    permission_required = "view_tipogasto"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(
                Q(nombre__icontains=q) | Q(descripcion__icontains=q),
                Q.OR
            )
        return TipoGasto.objects.filter(self.query).order_by("nombre")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("core:tipogasto_create")
        return ctx


class TipoGastoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = "core_AN/tipo_gasto/form.html"
    success_url = reverse_lazy("core:tipogasto_list")
    permission_required = "add_tipogasto"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Crear Tipo de Gasto"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Tipo de Gasto '{self.object.nombre}' creado correctamente.")
        return response


class TipoGastoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = "core_AN/tipo_gasto/form.html"
    success_url = reverse_lazy("core:tipogasto_list")
    permission_required = "change_tipogasto"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Tipo de Gasto"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Tipo de Gasto '{self.object.nombre}' actualizado correctamente.")
        return response


class TipoGastoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoGasto
    template_name = "core/delete.html"
    success_url = reverse_lazy("core:tipogasto_list")
    permission_required = "delete_tipogasto"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Tipo de Gasto"
        ctx["description"] = f"¿Desea eliminar el tipo de gasto '{self.object.nombre}'?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Tipo de Gasto '{nombre}' eliminado correctamente.")
        return response
