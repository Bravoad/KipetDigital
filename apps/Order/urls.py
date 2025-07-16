from .views import TypeServiceViewSet,OrderServiceViewSet,BudgetViewSet
from django.urls import path
urlpatterns = [
    path('budget/', BudgetViewSet.as_view(), name='budget-list'),
    path('service/', TypeServiceViewSet.as_view(), name='budget-list'),
    path('', OrderServiceViewSet.as_view(), name='order-create-list')
]
