from rest_framework import generics

from .models import Mission
from .serializers import MissionSerializer


class MissionListView(generics.ListCreateAPIView):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()


class MissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()
