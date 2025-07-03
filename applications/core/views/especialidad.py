from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.core.models import Especialidad
from applications.core.form_AN.especialidad import EspecialidadForm


class EspecialidadListView(PermissionMixin, ListViewMixin, ListView):
    model = Especialidad
    template_name = "core_AN/especialidades/list.html"
    context_object_name = "especialidades"
    permission_required = "view_especialidad"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(
                Q(nombre__icontains=q) | Q(descripcion__icontains=q),
                Q.OR
            )
        return Especialidad.objects.filter(self.query).order_by("nombre")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("core:especialidad_create")
        return ctx


class EspecialidadCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "core_AN/especialidades/form.html"
    success_url = reverse_lazy("core:especialidad_list")
    permission_required = "add_especialidad"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Crear Especialidad"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Especialidad {self.object.nombre} creada correctamente.")
        return response


class EspecialidadUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "core_AN/especialidades/form.html"
    success_url = reverse_lazy("core:especialidad_list")
    permission_required = "change_especialidad"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Especialidad"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Especialidad {self.object.nombre} actualizada correctamente.")
        return response


class EspecialidadDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Especialidad
    template_name = "core/delete.html"
    success_url = reverse_lazy("core:especialidad_list")
    permission_required = "delete_especialidad"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Especialidad"
        ctx["description"] = f"¿Desea eliminar la especialidad {self.object.nombre}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Especialidad {nombre} eliminada correctamente.")
        return response
