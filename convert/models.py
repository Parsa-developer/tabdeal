from django.db import models

# Create your models here.

class Convert(models.Model):
    number = models.IntegerField()
    to = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.number} - {self.to}"