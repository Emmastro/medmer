from django.db import models


# Create your models here.
class Patient(models.Model):
    email = models.EmailField()
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)

class Meta:
    ordering = ['created']


