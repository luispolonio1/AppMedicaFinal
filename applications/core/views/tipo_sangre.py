from django.http import JsonResponse
from django.db.models import Q
from applications.core.models import TipoSangre
from applications.core.form_s.tipo_sangre import TipoSangreForm
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

class TipoSangreListView(LoginRequiredMixin, ListView):
    model = TipoSangre
    template_name = 'core/tipo_sangre/list.html'  
    context_object_name = 'tiposangre'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['title'] = "Tipos de Sangre"
        context['permissions'] = {
            'add_tiposangre': user.has_perm('core.add_tiposangre'),
            'delete_tiposangre': user.has_perm('core.delete_tiposangre'),
        }
        return context
    
class TipoSangreCreateView(CreateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tipo_sangre/form.html'
    success_url = reverse_lazy('core:tipo_sangre_list')

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de sangre creado exitosamente.')
        return super().form_valid(form)
    
class TipoSangreDeleteView(DeleteView):
    model = TipoSangre
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:tipo_sangre_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Tipo de sangre eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
