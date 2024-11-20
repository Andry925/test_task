from django.db import models
from spycat.models import Cat


class Mission(models.Model):
    cat = models.ForeignKey(
        Cat,
        related_name='missions',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.targets.exists() and all(
                target.completed for target in self.targets.all()):
            self.completed = True
        super().save(*args, **kwargs)
