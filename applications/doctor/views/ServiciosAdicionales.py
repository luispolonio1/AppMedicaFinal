# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from applications.doctor.models import ServiciosAdicionales
from applications.doctor.forms.ServiciosAdicionales import ServiciosAdicionalesForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin


class ServiciosAdicionalesCreateView(PermissionMixin,CreateViewMixin,CreateView):
    model = ServiciosAdicionales
    form_class = ServiciosAdicionalesForm
    template_name = 'doctor/servicios/CrearServicio.html'
    success_url = reverse_lazy('home')
