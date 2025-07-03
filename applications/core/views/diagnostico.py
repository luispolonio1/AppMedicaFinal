from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.core.models import Diagnostico
from applications.core.form_AN.diagnostico import DiagnosticoForm


class DiagnosticoListView(PermissionMixin, ListViewMixin, ListView):
    model = Diagnostico
    template_name = "core_AN/diagnosticos/list.html"
    context_object_name = "diagnosticos"
    permission_required = "view_diagnostico"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(
                Q(codigo__icontains=q) | Q(descripcion__icontains=q),
                Q.OR
            )
        return Diagnostico.objects.filter(self.query).order_by("codigo")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("core:diagnostico_create")
        return ctx


class DiagnosticoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = "core_AN/diagnosticos/form.html"
    success_url = reverse_lazy("core:diagnostico_list")
    permission_required = "add_diagnostico"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Crear Diagnóstico"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Diagnóstico {self.object.codigo} creado correctamente.")
        return response


class DiagnosticoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = "core_AN/diagnosticos/form.html"
    success_url = reverse_lazy("core:diagnostico_list")
    permission_required = "change_diagnostico"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Diagnóstico"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Diagnóstico {self.object.codigo} actualizado correctamente.")
        return response


class DiagnosticoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Diagnostico
    template_name = "core/delete.html"
    success_url = reverse_lazy("core:diagnostico_list")
    permission_required = "delete_diagnostico"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Diagnóstico"
        ctx["description"] = f"¿Desea eliminar el diagnóstico {self.object.codigo} - {self.object.descripcion}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        codigo = self.object.codigo
        response = super().form_valid(form)
        messages.success(self.request, f"Diagnóstico {codigo} eliminado correctamente.")
        return response
