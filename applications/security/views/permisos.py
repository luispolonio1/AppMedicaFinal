# views.py
from django.views.generic import TemplateView
from applications.security.components.mixin_crud import PermissionMixin
from applications.security.models import Module
from django.contrib.auth.models import Permission
from django.http import JsonResponse

class PermissionDashboardView(PermissionMixin, TemplateView):
    template_name = 'security/permisos/permisos.html'


def get_permissions(request, pk):
    if request.method == "GET":
        try:
            module = Module.objects.get(pk=pk)
            permissions = module.permissions.all()

            data = [
                {"id": p.id, "name": p.name, "codename": p.codename}
                for p in permissions
            ]

            return JsonResponse(data, safe=False)

        except Module.DoesNotExist:
            return JsonResponse({"error": "Módulo no encontrado"}, status=404)


def get_all_permissions(request):
    if request.method == "GET":
        permissions = Permission.objects.all()
        data = [{"id": p.id, "name": p.name, "codename": p.codename} for p in permissions]
        return JsonResponse(data, safe=False)