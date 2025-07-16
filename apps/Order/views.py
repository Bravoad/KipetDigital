from django.shortcuts import render
from .models import Budget,TypeService,OrderService
from rest_framework import generics, mixins
from .serializer import BudgetSerializer, TypeServiceSerializer,OrderServiceSerializer


class BudgetViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TypeServiceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = TypeService.objects.all()
    serializer_class = TypeServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderServiceViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = OrderService.objects.all()
    serializer_class = OrderServiceSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
