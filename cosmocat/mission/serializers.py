from aim.models import Aim
from aim.serializers import AimSerializer
from rest_framework import serializers
from spycat.models import Cat

from .models import Mission


class MissionSerializer(serializers.ModelSerializer):
    cat = serializers.CharField(source='cat.name', read_only=True)
    targets = AimSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'completed', 'targets']

    def validate_cat(self, cat_name):
        try:
            return Cat.objects.get(name=cat_name)
        except Cat.DoesNotExist:
            raise serializers.ValidationError(f"No cat found with the name '{cat_name}'.")

    def create(self, validated_data):
        targets_data = validated_data.pop('targets', [])
        cat_name = validated_data.pop('cat')
        cat = self.validate_cat(cat_name)
        mission = Mission.objects.create(cat=cat, **validated_data)
        for target_data in targets_data:
            Aim.objects.create(mission=mission, **target_data)

        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', [])
        cat_name = validated_data.pop('cat', None)

        if cat_name:
            instance.cat = self.validate_cat(cat_name)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        existing_targets = {aim.id: aim for aim in instance.targets.all()}
        for target_data in targets_data:
            target_id = target_data.get('id')
            if target_id:
                target = existing_targets.pop(target_id, None)
                if target:
                    for attr, value in target_data.items():
                        setattr(target, attr, value)
                    target.save()
            else:
                Aim.objects.create(mission=instance, **target_data)

        for target in existing_targets.values():
            target.delete()

        return instance
