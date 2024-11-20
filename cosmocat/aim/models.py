from django.db import models
from mission.models import Mission


class Aim(models.Model):
    name = models.CharField(max_length=255)
    mission = models.ForeignKey(Mission, related_name='targets', on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'
