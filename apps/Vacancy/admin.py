from django.contrib import admin
from .models import Profession, Vacancy
# Register your models here.
@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['name']
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
