from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from applications.core.models import Paciente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from applications.core.form_s.pacientes import PacienteForm
from django.urls import reverse_lazy

class PacienteListView(ListView):
    model = Paciente
    template_name = 'core/pacientes/list.html'
    context_object_name = 'pacientes'


    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            return self.model.objects.filter(
                Q(nombres__icontains=q1) | Q(apellidos__icontains=q1)
            ).order_by('id')
        return self.model.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:paciente_create')
        user = self.request.user
        context['permissions'] = {
            'add_paciente': user.has_perm('core.add_paciente'),
            'change_paciente': user.has_perm('core.change_paciente'),
            'delete_paciente': user.has_perm('core.delete_paciente'),
            'view_paciente': user.has_perm('core.view_paciente'),
        }
        return context

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('core:paciente_list')

    def form_valid(self, form):
        messages.success(self.request, 'Paciente creado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Paciente'
        context['back_url'] = self.success_url
        return context
    
class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('core:paciente_list')

    def form_valid(self, form):
        messages.success(self.request, 'Paciente actualizado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Paciente'
        context['back_url'] = self.success_url
        return context

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'core/pacientes/confirm_delete.html'
    success_url = reverse_lazy('core:paciente_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Paciente eliminado correctamente.')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        return context