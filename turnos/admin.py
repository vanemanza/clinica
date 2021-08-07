from django.contrib import admin
from .models import Turnos

#class TurnosAdmin(admin.ModelAdmin):
 #   readonly_fields=('created')

admin.site.register(Turnos)