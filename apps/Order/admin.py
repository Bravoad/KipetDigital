from django.contrib import admin
from .models import OrderService, TypeService, Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderService)
class OrderServiceAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    pass