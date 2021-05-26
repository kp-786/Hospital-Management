from django.contrib import admin
from .models import *
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['status']

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Prescription)