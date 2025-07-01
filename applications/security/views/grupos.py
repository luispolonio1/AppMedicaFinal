from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.security.forms.grupos_F import GroupForm
from applications.security.models import Group

class GroupListView(PermissionMixin, ListViewMixin, ListView):
    model = Group
    template_name = "security/grupos/list.html"
    context_object_name = "groups"
    permission_required = "security.view_group"

    def get_queryset(self):
        return super().get_queryset().order_by("name")
    
class GroupCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = "security/grupos/form.html"
    success_url = reverse_lazy("security:grupos_list")
    permission_required = "security.add_group"

    def form_valid(self, form):
        messages.success(self.request, "Grupo creado exitosamente.")
        return super().form_valid(form)
    
class GroupUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "security/grupos/form.html"
    success_url = reverse_lazy("security:grupos_list")
    permission_required = "security.change_group"

    def form_valid(self, form):
        messages.success(self.request, "Grupo actualizado exitosamente.")
        return super().form_valid(form)
    
class GroupDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Group
    template_name = "security/grupos/delete.html"
    success_url = reverse_lazy("security:grupos_list")
    permission_required = "security.delete_group"

    def form_valid(self, form):
        messages.success(self.request, "Grupo eliminado exitosamente.")
        return super().form_valid(form)
