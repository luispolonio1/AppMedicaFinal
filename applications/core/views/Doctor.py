from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from applications.core.models import Doctor
from applications.core.forms_l.Doctor import DoctorForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin

class DoctorListView(PermissionMixin,ListViewMixin,ListView):
    model = Doctor
    template_name = 'core_l/Doctor/doctor_list.html'
    context_object_name = 'doctores'
    paginate_by = 10
    ordering = ['-id']

class DoctorCreateView(PermissionMixin,CreateViewMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core_l/Doctor/doctor_form.html'
    success_url = reverse_lazy('core:doctor_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Doctor {form.cleaned_data["nombres"]} {form.cleaned_data["apellidos"]} creado exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corrige los errores en el formulario.')
        return super().form_invalid(form)

class DoctorUpdateView(PermissionMixin,UpdateViewMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core_l/Doctor/doctor_form.html'
    success_url = reverse_lazy('core:doctor_list')
    
    def form_valid(self, form):
        messages.success(self.request, f'Doctor {form.cleaned_data["nombres"]} {form.cleaned_data["apellidos"]} actualizado exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor corrige los errores en el formulario.')
        return super().form_invalid(form)

class DoctorDeleteView(PermissionMixin,DeleteViewMixin, DeleteView):
    model = Doctor
    template_name = 'core_l/Doctor/doctor_confirm_delete.html'
    success_url = reverse_lazy('core:doctor_list')
    
    def delete(self, request, *args, **kwargs):
        doctor = self.get_object()
        doctor_name = f"{doctor.nombres} {doctor.apellidos}"
        messages.success(request, f'Doctor {doctor_name} eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)