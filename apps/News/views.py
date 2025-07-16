from rest_framework import generics, mixins
from .models import News
from .serializer import NewsSerializer


class NewsListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
