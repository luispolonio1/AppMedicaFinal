from django.urls import path
from . import views

app_name = 'citas'

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('crear/', views.crear_cita, name='crear_cita'),
]
