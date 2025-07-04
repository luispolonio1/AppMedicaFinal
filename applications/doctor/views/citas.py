import json
from decimal import Decimal

from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from applications.doctor.forms.citas import CitaMedicaForm
from applications.core.models import Paciente,Doctor
from applications.doctor.models import CitaMedica, HorarioAtencion
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q


class CitaMedicaListView(PermissionMixin, ListViewMixin, ListView):
    model = CitaMedica
    template_name = 'doctor/citas/list.html'
    permission_required = 'doctor.view_citamedica'
    context_object_name = 'citas'

    def get_queryset(self):
        user = self.request.user
        # Si es superusuario, ve todas las citas
        if user.is_superuser:
            return CitaMedica.objects.all().order_by('-fecha')

        # Si es un usuario normal, filtra por paciente o médico
        return CitaMedica.objects.filter(
            Q(paciente__user=user) |
            Q(medico__user=user)
        ).order_by('-fecha')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Citas Médicas'
        context['url_create'] = reverse_lazy('doctor:cita_create')
        context['url_delete'] = reverse_lazy('doctor:cita_delete')
        return context

class CitaMedicaCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = CitaMedica
    template_name = 'doctor/citas/form.html'
    permission_required = 'doctor.add_citamedica'
    success_url = reverse_lazy('doctor:cita_list')
    form_class = CitaMedicaForm

    def form_valid(self, form):
        with transaction.atomic():
            cita = form.save(commit=False)
            cita.fecha_creacion = timezone.now()
            cita.save()
            messages.success(self.request, 'Cita médica creada exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Cita Médica'
        context['form'] = self.get_form()
        context['pacientes'] = Paciente.objects.all()
        context['doctores'] = Doctor.objects.all()
        
        # Obtener horarios activos y convertirlos a formato útil para el frontend
        horarios = HorarioAtencion.objects.filter(activo=True)
        horarios_data = []
        
        for horario in HorarioAtencion.objects.filter(activo=True):
        # Normaliza los nombres de días quitando tildes y convirtiendo a minúsculas
            dia_semana = horario.dia_semana.lower()
            dia_semana = dia_semana.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
            
            horarios_data.append({
                'dia_semana': dia_semana,  # Ej: "miercoles"
                'hora_inicio': horario.hora_inicio.strftime('%H:%M'),
                'hora_fin': horario.hora_fin.strftime('%H:%M'),
                'intervalo_desde': horario.intervalo_desde.strftime('%H:%M') if horario.intervalo_desde else None,
                'intervalo_hasta': horario.intervalo_hasta.strftime('%H:%M') if horario.intervalo_hasta else None
            })
        
        context['horarios_json'] = json.dumps(horarios_data)
        return context

class CitaMedicaUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = CitaMedica
    template_name = 'doctor/citas/form.html'
    permission_required = 'doctor.change_citamedica'
    raise_exception = True  # Esto muestra 403 si no tiene permiso
    success_url = reverse_lazy('doctor:cita_list')
    form_class = CitaMedicaForm

    def get_queryset(self):
        user = self.request.user
        # Superusuarios pueden editar cualquier cita
        if user.is_superuser:
            return CitaMedica.objects.all()
        # Otros usuarios sólo pueden editar si son el paciente o el médico asociado
        return CitaMedica.objects.filter(
            Q(paciente__user=user) |
            Q(medico__user=user)
        )

    def form_valid(self, form):
        with transaction.atomic():
            cita = form.save(commit=False)
            cita.fecha_modificacion = timezone.now()
            cita.save()
            messages.success(self.request, 'Cita médica actualizada exitosamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Cita Médica'
        return context

class CitaMedicaDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = CitaMedica
    template_name = 'doctor/citas/delete.html'
    permission_required = 'doctor.delete_citamedica'
    success_url = reverse_lazy('doctor:cita_list')

    def delete(self, request, *args, **kwargs):
        with transaction.atomic():
            self.object = self.get_object()
            self.object.delete()
            messages.success(request, 'Cita médica eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cita Médica'
        return context
    

# VISTA CORREGIDA - views.py
class CitaMedicaDetailView(PermissionMixin, DetailView):  # Cambié ListView por DetailView
    model = CitaMedica
    template_name = 'doctor/citas/detalle.html'  # Corregí el nombre del template
    permission_required = 'doctor.view_citamedica'
    context_object_name = 'cita'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente = self.object.paciente
        context['title'] = 'Detalle de Cita Médica'
        context['paciente'] = paciente

        # Prepara lista de tuplas para la ficha clínica
        context['ficha_clinica'] = [
            ("Antecedentes Personales", paciente.antecedentes_personales),
            ("Antecedentes Quirúrgicos", paciente.antecedentes_quirurgicos),
            ("Antecedentes Familiares", paciente.antecedentes_familiares),
            ("Alergias", paciente.alergias),
            ("Medicamentos Actuales", paciente.medicamentos_actuales),
            ("Hábitos Tóxicos", paciente.habitos_toxicos),
            ("Vacunas", paciente.vacunas),
            ("Antecedentes Gineco-Obstétricos", paciente.antecedentes_gineco_obstetricos),
        ]

        return context
