from rest_framework import generics, mixins
from .models import Profession,Vacancy
from .serializer import ProfessionSerializer,VacancySerializer


class ProfessionListApiView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class VacancyListCreateAPIView(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
