from django.db import models

# Create your models here.


class SiteSettingModel(models.Model):
	site_name = models.CharField(max_length=200)
	site_url = models.CharField(max_length=250)
	address = models.TextField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=12, null=True, blank=True)
	is_active = models.BooleanField()
	about = models.TextField(null=True, blank=True)

