from rest_framework import serializers
from .models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Technology
        fields = '__all__'
