from django.db import models
from django.contrib.auth.models import User


class Medic(User):

    country = models.CharField(max_length=120)
    medic_id = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
