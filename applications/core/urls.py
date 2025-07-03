from django.urls import path
from applications.core.views.paciente import paciente_find
from applications.core.views.pacientes import PacienteCreateView, PacienteListView, PacienteUpdateView, PacienteDeleteView
from applications.core.views.tipo_sangre import TipoSangreCreateView, TipoSangreListView, TipoSangreDeleteView
from applications.core.views.Gastomensual import GastomensualListView, GastomensualCreateView, GastomensualUpdateView, GastomensualDeleteView

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name="paciente_find"),

    path('paciente_list/', PacienteListView.as_view(), name='paciente_list'),
    path('paciente_create/', PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente_update/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('paciente_delete/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_delete'),

    
    path('tipo_sangre_list/', TipoSangreListView.as_view(), name='tipo_sangre_list'),
    path('tipo_sangre_create/',TipoSangreCreateView.as_view(), name='tipo_sangre_create'),
    path('tipo_sangre_delete/<int:pk>/', TipoSangreDeleteView.as_view(), name='tipo_sangre_delete'),

    # Rutas para vistas relacionadas con Gastos Mensuales
    path('gastomensual_list/', GastomensualListView.as_view(), name='gastomensual_list'),
    path('gastomensual_create/', GastomensualCreateView.as_view(), name='gastomensual_create'),
    path('gastomensual_update/<int:pk>/', GastomensualUpdateView.as_view(), name='gastomensual_update'),
    path('gastomensual_delete/<int:pk>/', GastomensualDeleteView.as_view(), name='gastomensual_delete'),    
]