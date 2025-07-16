from .views import NewsListApiView
from django.urls import path
urlpatterns = [
    path('', NewsListApiView.as_view(), name='news-list')
]