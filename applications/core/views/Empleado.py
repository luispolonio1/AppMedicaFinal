from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from applications.core.models import Empleado
from applications.core.forms_l.Empleado import EmpleadoForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin

class EmpleadoListView(PermissionMixin,ListViewMixin,ListView):
    model = Empleado
    template_name = 'core_l/Empleado/empleado_list.html'
    context_object_name = 'empleados'
    paginate_by = 10
    
    def get_queryset(self):
        return Empleado.objects.filter(activo=True).order_by('nombres')


class EmpleadoCreateView(PermissionMixin,CreateViewMixin,CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core_l/Empleado/empleado_form.html'
    success_url = reverse_lazy('core:empleado_list')
    
    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)