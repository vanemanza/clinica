from django.contrib import admin
from .models import Pacientes, Domicilio

class PacientesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'created']    
    list_filter = ['apellido']
    search_fields = ['email', 'nombre']
    class Meta:
        model = Pacientes

admin.site.register(Domicilio)
admin.site.register(Pacientes, PacientesAdmin)
