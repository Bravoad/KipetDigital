from rest_framework import serializers
from .models import OrderService, Budget, TypeService


class BudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Budget
        fields = (
            'id', 'name', 'is_displayed', 'order'
        )


class TypeServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeService
        fields = (
            'id', 'name', 'is_displayed', 'order'
        )


class OrderServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderService
        fields = (
            'id', 'types_services', 'name', 'company', 'phone', 'email',
            'budget', 'comment', 'file'
        )
        read_only_fields = ('id',)
