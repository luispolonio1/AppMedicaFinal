from django.urls import path
from applications.doctor.views.atencion_medica import AtencionListView, AtencionCreateView, AtencionUpdateView, \
    AtencionDeleteView
from applications.doctor.views.citas import CitaMedicaListView, CitaMedicaCreateView, CitaMedicaUpdateView, CitaMedicaDeleteView,\
    CitaMedicaDetailView

from applications.doctor.views.AtencionCita import AtenderPacienteView, AtencionDetailView

from applications.doctor.views.pago import PagoListView, PagoCreateView, PagoUpdateView, PagoDeleteView
from applications.doctor.views.detalle_pago import DetallePagoListView, DetallePagoCreateView, \
    DetallePagoUpdateView, DetallePagoDeleteView    


from applications.doctor.views.horario_atencion import HorarioAtencionListView, HorarioAtencionCreateView, \
    HorarioAtencionUpdateView, HorarioAtencionDeleteView    

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
    path('atencion/<int:pk>/', AtencionDetailView.as_view(), name="atencion_detail"),
    
    path("pago_list/", PagoListView.as_view()), 
    path("pagos/",            PagoListView.as_view(),   name="pago_list"),
    path("pagos/crear/",      PagoCreateView.as_view(), name="pago_create"),
    path("pagos/<int:pk>/",   PagoUpdateView.as_view(), name="pago_update"),
    path("pagos/<int:pk>/eliminar/", PagoDeleteView.as_view(), name="pago_delete"),

    path("detallepago_list/", DetallePagoListView.as_view()),
    path("detalles/", DetallePagoListView.as_view(), name="detallepago_list"),
    path("detalles/crear/", DetallePagoCreateView.as_view(), name="detallepago_create"),
    path("detalles/<int:pk>/", DetallePagoUpdateView.as_view(), name="detallepago_update"),
    path("detalles/<int:pk>/eliminar/", DetallePagoDeleteView.as_view(), name="detallepago_delete"),

    path("horario_list/", HorarioAtencionListView.as_view()),
    path("horarios/", HorarioAtencionListView.as_view(), name="horario_list"),
    path("horarios/crear/", HorarioAtencionCreateView.as_view(), name="horario_create"),
    path("horarios/<int:pk>/editar/", HorarioAtencionUpdateView.as_view(), name="horario_update"),
    path("horarios/<int:pk>/eliminar/", HorarioAtencionDeleteView.as_view(), name="horario_delete"),




]
