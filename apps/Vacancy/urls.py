from .views import ProfessionListApiView,VacancyListCreateAPIView
from django.urls import path
urlpatterns = [
    path('typepr/', ProfessionListApiView.as_view(), name='prof-list'),
    path('', VacancyListCreateAPIView.as_view(), name='vacancy-create-list')
]
