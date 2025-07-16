from rest_framework import generics, mixins
from .models import Service
from .serializer import ServiceSerializer


class ServiceListApiView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
