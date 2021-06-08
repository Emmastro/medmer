from django.db import models

class HelpRequest(models.Model):
    """ """
    STATUS = models.TextChoices('STATUS', "Pending Accepted Done")

    # TODO: medic should be able to perform help requests too
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    
    medic = models.ForeignKey('medic.Medic', on_delete=models.CASCADE)
    medic_notes = models.TextField()
    
    patient_notes = models.TextField()
    patient_location = models.CharField(max_length=120)

    time_requested = models.DateTimeField(auto_now_add=True)
    time_accepted = models.DateTimeField()
    time_concluded = models.DateTimeField()
