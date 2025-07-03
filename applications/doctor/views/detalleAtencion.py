from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import DetalleAtencion
from applications.doctor.forms.detalleAtencion import DetalleAtencionForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin

class DetalleAtencionCreateView(PermissionMixin,CreateViewMixin,CreateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/atenciones/detalleAtencionForm.html'   # Cambia por tu template
    success_url = reverse_lazy('home')  # Cambia por tu nombre de URL
