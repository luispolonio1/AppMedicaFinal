from django.contrib import admin
from applications.doctor.models import CitaMedica

from django.contrib.admin.sites import AlreadyRegistered

try:
    admin.site.register(CitaMedica)
except AlreadyRegistered:
    pass 
