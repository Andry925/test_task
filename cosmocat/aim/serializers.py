from rest_framework import serializers

from .models import Aim


class AimSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Aim
        fields = ['id', 'name', 'notes', 'completed']
