from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.core.models import Cargo
from applications.core.form_AN.cargo import CargoForm


class CargoListView(PermissionMixin, ListViewMixin, ListView):
    model = Cargo
    template_name = "core_AN/cargos/list.html"
    context_object_name = "cargos"
    permission_required = "view_cargo"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(
                Q(nombre__icontains=q) | Q(descripcion__icontains=q),
                Q.OR
            )
        return Cargo.objects.filter(self.query).order_by("nombre")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("core:cargo_create")
        return ctx


class CargoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = "core_AN/cargos/form.html"
    success_url = reverse_lazy("core:cargo_list")
    permission_required = "add_cargo"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Crear Cargo"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Cargo {self.object.nombre} creado correctamente.")
        return response


class CargoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = "core_AN/cargos/form.html"
    success_url = reverse_lazy("core:cargo_list")
    permission_required = "change_cargo"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Cargo"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Cargo {self.object.nombre} actualizado correctamente.")
        return response


class CargoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Cargo
    template_name = "core/delete.html"
    success_url = reverse_lazy("core:cargo_list")
    permission_required = "delete_cargo"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Cargo"
        ctx["description"] = f"¿Desea eliminar el cargo {self.object.nombre}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Cargo {nombre} eliminado correctamente.")
        return response
