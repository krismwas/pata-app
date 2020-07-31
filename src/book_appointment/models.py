from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date


# Create your models here.
class BookAppoinment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    doctor = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dr_booked")
    timestamp = models.TimeField(auto_now=True)
    appointment_datee = models.DateField(default=date.today)
    # timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "%s" %(self.patient)


        # class BookAppointment(models.Model):
        #     patient = models.ForeignKey(settings.AUTH_USER_MODEL)
        #     doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="doctor_appointment")
        #     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        #     appointment_date = models.DateField(auto_now_add=False, auto_now=False)
