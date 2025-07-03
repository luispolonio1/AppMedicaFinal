from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from applications.core.models import TipoMedicamento
from applications.core.forms_l.TiposMedicamentos import TipoMedicamentoForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin

class TipoMedicamentoCreateView(PermissionMixin,CreateViewMixin,CreateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core_l/TipoMedicamento/TipoMedicamento.html'  # Ajusta la ruta según tu estructura
    success_url = reverse_lazy('home')  # Cambia por tu URL de listado
