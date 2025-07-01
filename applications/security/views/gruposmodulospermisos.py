from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.security.models import GroupModulePermission
from django.db.models import Q
from applications.security.forms.Gruposmodulospermisos_F import GroupModulePermissionForm

class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/gruposmodulospermisos/list.html'
    model = GroupModulePermission
    context_object_name = 'group_module_permissions'
    permission_required = 'view_groupmodulepermission'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(group__name__icontains=q1) | Q(module__name__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:group_module_permission_create')
        return context
    
class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    template_name = 'security/gruposmodulospermisos/form.html'
    model = GroupModulePermission
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'add_groupmodulepermission'

    def form_valid(self, form):
        messages.success(self.request, 'Grupo, módulo y permisos creados correctamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Grupo, Módulo y Permisos'
        context['back_url'] = self.success_url
        return context

class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    template_name = 'security/gruposmodulospermisos/form.html'
    model = GroupModulePermission
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'change_groupmodulepermission'

    def form_valid(self, form):
        messages.success(self.request, 'Grupo, módulo y permisos actualizados correctamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Grupo, Módulo y Permisos'
        context['back_url'] = self.success_url
        return context
    
class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    template_name = 'security/gruposmodulospermisos/delete.html'
    model = GroupModulePermission
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'delete_groupmodulepermission'

    def form_valid(self, form):
        messages.success(self.request, 'Grupo, módulo y permisos eliminados correctamente.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        return context