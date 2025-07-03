from django.urls import path
from applications.core.views.paciente import paciente_find
from applications.core.views.TipoMedicamento import TipoMedicamentoCreateView
from applications.core.views.MarcaMedicamento import MarcaMedicamentoCreateView
from applications.core.views.Medicamentos import MedicamentoCreateView
from applications.core.views.Empleado import EmpleadoCreateView,EmpleadoListView
from applications.core.views.Doctor import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name="paciente_find"),

    # Rutas para vistas relacionadas con TipoMedicamento
    path('tipo_medicamento', TipoMedicamentoCreateView.as_view(), name='tipo_medicamento_crear'),

    # Rutas para vistas relacionadas con MarcaMedicamento
    path('marca_medicamento', MarcaMedicamentoCreateView.as_view(), name='marca_medicamento_crear'),

    # Rutas para vistas relacionadas con Medicamentos
    path('medicamento_crear', MedicamentoCreateView.as_view(), name='medicamento_crear'),


    # Rutas para vistas relacionadas con Empleados
    path('empleado_crear', EmpleadoCreateView.as_view(), name='empleado_crear'),
    path('empleado_list', EmpleadoListView.as_view(), name='empleado_list'),

    # Rutas para vistas relacionadas con Doctores
    path('doctor_list', DoctorListView.as_view(), name='doctor_list'),
    path('doctor_create', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),

]