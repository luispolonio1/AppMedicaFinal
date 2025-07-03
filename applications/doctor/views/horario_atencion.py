from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.doctor.models import HorarioAtencion
from applications.doctor.forms.horario_atencion import HorarioAtencionForm


class HorarioAtencionListView(PermissionMixin, ListViewMixin, ListView):
    model = HorarioAtencion
    template_name = "doctor/horario_atencion/list.html"
    context_object_name = "horarios"
    permission_required = "view_horarioatencion"

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            self.query.add(Q(dia_semana__icontains=q), Q.OR)
        return HorarioAtencion.objects.filter(self.query).order_by("dia_semana")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["create_url"] = reverse_lazy("doctor:horario_create")
        return ctx


class HorarioAtencionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = HorarioAtencion
    form_class = HorarioAtencionForm
    template_name = "doctor/horario_atencion/form.html"
    success_url = reverse_lazy("doctor:horario_list")
    permission_required = "add_horarioatencion"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Crear Horario"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Horario creado correctamente.")
        return response


class HorarioAtencionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = HorarioAtencion
    form_class = HorarioAtencionForm
    template_name = "doctor/horario_atencion/form.html"
    success_url = reverse_lazy("doctor:horario_list")
    permission_required = "change_horarioatencion"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Actualizar Horario"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Horario actualizado correctamente.")
        return response


class HorarioAtencionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = HorarioAtencion
    template_name = "doctor/delete.html"
    success_url = reverse_lazy("doctor:horario_list")
    permission_required = "delete_horarioatencion"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["grabar"] = "Eliminar Horario"
        ctx["description"] = f"¿Desea eliminar el horario de {self.object.dia_semana}?"
        ctx["back_url"] = self.success_url
        return ctx

    def form_valid(self, form):
        dia = self.object.dia_semana
        response = super().form_valid(form)
        messages.success(self.request, f"Horario de {dia} eliminado correctamente.")
        return response
