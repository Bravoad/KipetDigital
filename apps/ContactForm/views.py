from rest_framework import generics, mixins
from .models import ContactForm
from .serializer import ContactFormSerializer

# Create your views here.


class ContactFormListCreateApiView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
