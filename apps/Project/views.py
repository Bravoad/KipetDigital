from rest_framework import generics, mixins
from .models import TypeProject,Project
from .serializer import TypeProjectSerializer,ProjectSerializer


class TypeProjectListApiView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = TypeProject.objects.all()
    serializer_class = TypeProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectListApiView(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
