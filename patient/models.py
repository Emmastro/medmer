from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Patient(User):

    age = models.IntegerField()
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=30, choices=[('Male','male'),('Female','female')])
