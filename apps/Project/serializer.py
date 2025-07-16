from rest_framework import serializers
from .models import TypeProject,Project


class TypeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    typeProject = TypeProjectSerializer()
    class Meta:
        model = Project
        fields = '__all__'
