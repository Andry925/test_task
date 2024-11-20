from django.core.exceptions import ValidationError
from django.db import models

from .tasks import get_available_greeds

URL = "https://api.thecatapi.com/v1/breeds"


class Cat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.PositiveIntegerField(default=1)
    experience = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    salary = models.PositiveIntegerField(default=0, )
    breed = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.breed = self.validate_cat_breed()
        super().save(*args, **kwargs)

    def validate_cat_breed(self):
        if self.breed not in get_available_greeds(URL):
            raise ValidationError("This breed is not available")
        return self.breed
