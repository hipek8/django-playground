from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id}, name={self.name})"
