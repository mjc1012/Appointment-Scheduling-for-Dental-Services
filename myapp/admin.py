from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Dentist)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Procedure)
admin.site.register(Record)
