from .views import TechnologyListApiView
from django.urls import path
urlpatterns = [
    path('', TechnologyListApiView.as_view(), name='technology-list')
]
