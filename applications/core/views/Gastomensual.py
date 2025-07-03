from django.http import JsonResponse
from django.db.models import Q
from applications.core.models import GastoMensual
from applications.core.form_s.Gastomensual import GastoMensualForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

class GastomensualListView(LoginRequiredMixin, ListView):
    model = GastoMensual
    template_name = 'core/gastosmensual/list.html'
    context_object_name = 'gastos'

    def get_queryset(self):
        return GastoMensual.objects.all().order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['title'] = 'Listado de Gastos Mensuales'
        context['permissions'] = {
            'add_gastomensual': user.has_perm('core.add_gastomensual'),
            'change_gastomensual': user.has_perm('core.change_gastomensual'),
            'delete_gastomensual': user.has_perm('core.delete_gastomensual'),
        }
        return context

class GastomensualCreateView(PermissionRequiredMixin, CreateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gastosmensual/form.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'core.add_gastomensual'

    def form_valid(self, form):
        messages.success(self.request, 'Gasto mensual creado exitosamente.')
        return super().form_valid(form)


class GastomensualUpdateView(PermissionRequiredMixin, UpdateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gastosmensual/form.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'core.change_gastomensual'

    def form_valid(self, form):
        messages.success(self.request, 'Gasto mensual actualizado exitosamente.')
        return super().form_valid(form)


class GastomensualDeleteView(PermissionRequiredMixin, DeleteView):
    model = GastoMensual
    template_name = 'core/gastosmensual/delete.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'core.delete_gastomensual'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Gasto mensual eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)