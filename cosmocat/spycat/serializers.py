from rest_framework import serializers

from .models import Cat


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'


class UpdateCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = 'salary'
