from rest_framework import serializers
from .models import Profession, Vacancy


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    profession = ProfessionSerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'
