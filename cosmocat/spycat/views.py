from rest_framework import generics

from .models import Cat
from .serializers import SpyCatSerializer, UpdateCatSerializer


class SpycatListCreateView(generics.ListCreateAPIView):
    serializer_class = SpyCatSerializer
    queryset = Cat.objects.all()


class SpycatRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = SpyCatSerializer
    queryset = Cat.objects.all()


class SpycatUpdateView(generics.UpdateAPIView):
    serializer_class = UpdateCatSerializer
    queryset = Cat.objects.all()
