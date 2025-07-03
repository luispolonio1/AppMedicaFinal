# views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from applications.core.models import Medicamento
from applications.core.forms_l.Medicamentos import MedicamentoForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin


class MedicamentoCreateView(PermissionMixin,CreateViewMixin,CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core_l/medicamento/Medicamento_create.html'
    success_url = reverse_lazy('home')  # Ajusta según tu URL
    
    def form_valid(self, form):
        messages.success(self.request, 'Medicamento creado exitosamente.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el medicamento. Verifique los datos.')
        return super().form_invalid(form)