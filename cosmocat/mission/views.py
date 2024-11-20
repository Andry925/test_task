from django.core.exceptions import ValidationError
from rest_framework import generics
from spycat.models import Cat

from .models import Mission
from .serializers import MissionSerializer


class MissionListView(generics.ListCreateAPIView):
    serializer_class = MissionSerializer

    def get_queryset(self):
        return Mission.objects.select_related('cat').prefetch_related('targets')

    def perform_create(self, serializer):
        cat_name = self.request.data.get('cat')
        try:
            cat_obj = Cat.objects.get(name=cat_name)
        except Cat.DoesNotExist:
            raise ValidationError(f"No cat found with the name '{cat_name}'.")

        if Mission.objects.filter(cat=cat_obj).count() >= 3:
            raise ValidationError("A cat cannot have more than 3 missions.")
        serializer.save(cat=cat_obj)


class MissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MissionSerializer

    def get_queryset(self):
        return Mission.objects.select_related('cat').prefetch_related('targets')

    def perform_update(self, serializer):
        current_obj = self.get_object()

        if current_obj.completed:
            raise ValidationError("You cannot edit completed missions.")
