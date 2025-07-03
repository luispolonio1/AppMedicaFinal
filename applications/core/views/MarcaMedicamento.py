# views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from applications.core.models import MarcaMedicamento
from applications.core.forms_l.MarcaMedicamento import MarcaMedicamentoForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin



class MarcaMedicamentoCreateView(PermissionMixin,CreateViewMixin,CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core_l/MarcaMedicamento/MarcaMedicamentoCreate.html'
    success_url = reverse_lazy('home')  # Ajusta según tu URL
    
    def form_valid(self, form):
        messages.success(self.request, 'Marca de medicamento creada exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear la marca de medicamento. Verifique los datos.')
        return super().form_invalid(form)