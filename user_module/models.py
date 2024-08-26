from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from product_module.models import ProductModel
# Create your models here.
from first import settings


class UserModel(AbstractUser):
    email_active_code = models.CharField(max_length=128, default='')
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username


class CommentModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("home-page")


