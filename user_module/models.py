from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserModel(AbstractUser):
    email_active_code = models.CharField(max_length=128, default='')
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username