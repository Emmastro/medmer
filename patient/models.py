from django.db import models
from django.contrib.auth.models import User


class Patient(User):

    age = models.IntegerField()
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=30, choices=[('Male','male'),('Female','female')])
