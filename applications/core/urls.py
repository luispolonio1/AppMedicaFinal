from django.urls import path
from applications.core.views.paciente import paciente_find
from applications.core.views.diagnostico import (
    DiagnosticoListView, DiagnosticoCreateView,
    DiagnosticoUpdateView, DiagnosticoDeleteView
)
from applications.core.views.tipogasto import (
    TipoGastoListView, TipoGastoCreateView,
    TipoGastoUpdateView, TipoGastoDeleteView    )


from applications.core.views.foto_paciente import (
    FotoPacienteListView, FotoPacienteCreateView,
    FotoPacienteUpdateView, FotoPacienteDeleteView) 


from applications.core.views.cargo import (
    CargoListView, CargoCreateView,
    CargoUpdateView, CargoDeleteView)

from applications.core.views.especialidad import (
    EspecialidadListView, EspecialidadCreateView,
    EspecialidadUpdateView, EspecialidadDeleteView)


app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name="paciente_find"),
    path("diagnostico_list/", DiagnosticoListView.as_view()), 
    path("diagnosticos/", DiagnosticoListView.as_view(), name="diagnostico_list"),
    path("diagnosticos/crear/", DiagnosticoCreateView.as_view(), name="diagnostico_create"),
    path("diagnosticos/<int:pk>/", DiagnosticoUpdateView.as_view(), name="diagnostico_update"),
    path("diagnosticos/<int:pk>/eliminar/", DiagnosticoDeleteView.as_view(), name="diagnostico_delete"),

    path("tipogasto_list/", TipoGastoListView.as_view()), 
    path("tipo-gasto/", TipoGastoListView.as_view(), name="tipogasto_list"),
    path("tipo-gasto/crear/", TipoGastoCreateView.as_view(), name="tipogasto_create"),
    path("tipo-gasto/<int:pk>/editar/", TipoGastoUpdateView.as_view(), name="tipogasto_update"),
    path("tipo-gasto/<int:pk>/eliminar/", TipoGastoDeleteView.as_view(), name="tipogasto_delete"),    path("fotos/", FotoPacienteListView.as_view(), name="foto_list"),

    path("foto_list/", FotoPacienteListView.as_view()), 
    path("fotos/", FotoPacienteListView.as_view(), name="foto_list"),
    path("fotos/crear/", FotoPacienteCreateView.as_view(), name="foto_create"),
    path("fotos/<int:pk>/editar/", FotoPacienteUpdateView.as_view(), name="foto_update"),
    path("fotos/<int:pk>/eliminar/", FotoPacienteDeleteView.as_view(), name="foto_delete"),

    path("cargo_list/", CargoListView.as_view()), 
    path("cargos/", CargoListView.as_view(), name="cargo_list"),
    path("cargos/crear/", CargoCreateView.as_view(), name="cargo_create"),
    path("cargos/<int:pk>/editar/", CargoUpdateView.as_view(), name="cargo_update"),
    path("cargos/<int:pk>/eliminar/", CargoDeleteView.as_view(), name="cargo_delete"),
   
    path("especialidad_list/", EspecialidadListView.as_view()),
    path("especialidades/", EspecialidadListView.as_view(), name="especialidad_list"),
    path("especialidades/crear/", EspecialidadCreateView.as_view(), name="especialidad_create"),
    path("especialidades/<int:pk>/editar/", EspecialidadUpdateView.as_view(), name="especialidad_update"),
    path("especialidades/<int:pk>/eliminar/", EspecialidadDeleteView.as_view(), name="especialidad_delete"),
]







