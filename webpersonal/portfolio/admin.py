from django.contrib import admin
from .models import Project
# Register your models here.

#Se crea una clase para los campos de fecha que solo puedan verse sin editar
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

admin.site.register(Project, ProjectAdmin)