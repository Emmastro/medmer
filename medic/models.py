from django.db import models


# Create your models here.
class Medic(models.Model):
    email = models.EmailField()
    medic_id = models.IntegerField()
    name = models.CharField(max_length=100)
    Speciality = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Meta:
    ordering = ['created']


