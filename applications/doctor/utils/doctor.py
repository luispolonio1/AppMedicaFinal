from django.db import models


class DiaSemanaChoices(models.TextChoices):
    LUNES = 'lunes', 'Lunes'
    MARTES = 'martes', 'Martes'
    MIERCOLES = 'miercoles', 'Miercoles'
    JUEVES = 'jueves', 'Jueves'
    VIERNES = 'viernes', 'Viernes'
    SABADO = 'sabado', 'Sabado'
    DOMINGO = 'domingo', 'Domingo'