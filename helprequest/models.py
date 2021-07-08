from django.db import models
from autoslug import AutoSlugField

class HelpRequest(models.Model):
    """ """
    STATUS = models.TextChoices('STATUS', "Pending Accepted Done")

    # TODO: medic should be able to perform help requests too
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    slug = AutoSlugField(unique_with='id', populate_from='patient')
    medic = models.ForeignKey('medic.Medic', on_delete=models.CASCADE, blank=True, null=True)
    medic_notes = models.TextField(blank=True, null=True)
    
    patient_notes = models.TextField(blank=True, null=True)
    patient_location = models.CharField(max_length=120, blank=True, null=True)

    time_requested = models.DateTimeField(auto_now_add=True)
    time_accepted = models.DateTimeField(blank=True, null=True)
    time_concluded = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.patient, self.time_requested)