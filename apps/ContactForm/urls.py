from .views import ContactFormListCreateApiView
from django.urls import path
urlpatterns = [
    path('', ContactFormListCreateApiView.as_view(), name='contact-form-list')
]