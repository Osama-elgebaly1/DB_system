from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

