from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.security.forms.users import CustomUserEditForm 
from applications.security.forms.registro import CustomUserCreationForm

User= get_user_model()  

# Listado de usuarios
class UserListView(PermissionMixin, ListViewMixin, ListView):
    model = User
    template_name = 'security/users/list.html'
    context_object_name = 'users'
    permission_required = 'view_user'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(username__icontains=q), Q.OR)
            self.query.add(Q(email__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:user_create')
        return context

# Crear usuario
class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'security/users/form.html'
    success_url = reverse_lazy('security:user_list')  # <- Asegúrate de que esta URL esté bien

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Usuario {self.object.username} creado con éxito.')
        return response


# Editar usuario
class UserUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = User
    form_class = CustomUserEditForm
    template_name = 'security/users/form.html'
    success_url = reverse_lazy('security:user_list')
    permission_required = 'change_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Usuario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Usuario {self.object.username} actualizado correctamente.')
        return response


# Eliminar usuario
class UserDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = User
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:user_list')
    permission_required = 'delete_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Usuario'
        context['description'] = f'¿Desea eliminar al usuario {self.object.username}?'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        username = self.object.username
        response = super().form_valid(form)
        messages.success(self.request, f'Usuario {username} eliminado correctamente.')
        return response
