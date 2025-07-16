from rest_framework import generics, mixins
from .models import Technology
from .serializer import TechnologySerializer


class TechnologyListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
