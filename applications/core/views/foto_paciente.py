from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.core.models import FotoPaciente
from applications.core.form_AN.foto_paciente import FotoPacienteForm


class FotoPacienteListView(PermissionMixin, ListViewMixin, ListView):
    model = FotoPaciente
    template_name = "core_AN/foto_paciente/list.html"
    context_object_name = "fotos"
    permission_required = "view_fotopaciente"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(Q(paciente__nombres__icontains=q) | Q(descripcion__icontains=q), Q.OR)
        return FotoPaciente.objects.filter(self.query).select_related('paciente').order_by("-fecha_subida")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("core:foto_create")
        return ctx


class FotoPacienteCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = FotoPaciente
    form_class = FotoPacienteForm
    template_name = "core_AN/foto_paciente/form.html"
    success_url = reverse_lazy("core:foto_list")
    permission_required = "add_fotopaciente"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Subir Nueva Foto"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Foto subida correctamente.")
        return response


class FotoPacienteUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = FotoPaciente
    form_class = FotoPacienteForm
    template_name = "core_AN/foto_paciente/form.html"
    success_url = reverse_lazy("core:foto_list")
    permission_required = "change_fotopaciente"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Foto"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Foto actualizada correctamente.")
        return response


class FotoPacienteDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = FotoPaciente
    template_name = "core/delete.html"
    success_url = reverse_lazy("core:foto_list")
    permission_required = "delete_fotopaciente"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Foto"
        ctx["description"] = f"¿Desea eliminar la imagen de {self.object.paciente}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        paciente = self.object.paciente
        response = super().form_valid(form)
        messages.success(self.request, f"Foto de {paciente} eliminada correctamente.")
        return response
