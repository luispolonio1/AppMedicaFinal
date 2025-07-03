from django.urls import path
from applications.doctor.views.atencion_medica import AtencionListView, AtencionCreateView, AtencionUpdateView, \
    AtencionDeleteView
from applications.doctor.views.citas import CitaMedicaListView, CitaMedicaCreateView, CitaMedicaUpdateView, CitaMedicaDeleteView,\
    CitaMedicaDetailView

from applications.doctor.views.AtencionCita import AtenderPacienteView,ObtenerHorariosDisponiblesView
from applications.doctor.views.detalleAtencion import DetalleAtencionCreateView
from applications.doctor.views.ServiciosAdicionales import ServiciosAdicionalesCreateView
app_name='doctor' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Doctor
    path('atencion_list/', AtencionListView.as_view(), name="atencion_list"),
    path('atencion_create/', AtencionCreateView.as_view(), name="atencion_create"),
    path('atencion_update/<int:pk>/', AtencionUpdateView.as_view(), name="atencion_update"),
    path('atencion_delete/<int:pk>/', AtencionDeleteView.as_view(), name="atencion_delete"),


    # Rutas para vistas relacionadas con Citas Medicas
    path('cita_list/', CitaMedicaListView.as_view(), name="cita_list"),
    path('cita_create/', CitaMedicaCreateView.as_view(), name="cita_create"),
    path('cita_update/<int:pk>/', CitaMedicaUpdateView.as_view(), name="cita_update"),
    path('cita_delete/<int:pk>/', CitaMedicaDeleteView.as_view(), name="cita_delete"),
    path('cita_detail/<int:pk>/', CitaMedicaDetailView.as_view(), name="cita_detail"),

    # Rutas para vistas relacionadas con Atencion de Citas
    path('cita/<int:pk>/atender/', AtenderPacienteView.as_view(), name="atender_paciente"),
    path('horarios/disponibles/', ObtenerHorariosDisponiblesView.as_view(), name='obtener_horarios'),

    # Ruta para crear Detalle de Atencion
    path('detalle_atencion', DetalleAtencionCreateView.as_view(), name='detalle_atencion_create'),

    # Rutas para Servicios Adicionales
    path('servicios_adicionales', ServiciosAdicionalesCreateView.as_view(), name='servicios_adicionales_create'),
]