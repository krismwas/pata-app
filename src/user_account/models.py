from django.db import models

# Create your models here.
from django.conf import settings


class UserAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
