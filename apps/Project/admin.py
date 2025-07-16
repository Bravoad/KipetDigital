from django.contrib import admin
from .models import Project,TypeProject
# Register your models here.


@admin.register(TypeProject)
class TypeProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_displayed']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_displayed']
