from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Medic(User):

    country = models.CharField(max_length=120)
    medic_id = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Medic.objects.create(user=instance)
    instance.profile.save()