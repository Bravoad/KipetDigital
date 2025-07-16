from .views import ProjectListApiView,TypeProjectListApiView
from django.urls import path
urlpatterns = [
    path('typepr/', TypeProjectListApiView.as_view(), name='type-project-list'),
    path('', ProjectListApiView.as_view(), name='project-list')
]