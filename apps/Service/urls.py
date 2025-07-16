from .views import ServiceListApiView
from django.urls import path
urlpatterns = [
    path('', ServiceListApiView.as_view(), name='service-list')
]