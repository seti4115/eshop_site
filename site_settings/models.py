from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
from django.utils.text import slugify


class SiteSettingModel(models.Model):
	site_name = models.CharField(max_length=200)
	site_url = models.CharField(max_length=250)
	address = models.TextField(null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=12, null=True, blank=True)
	is_active = models.BooleanField()
	about = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.site_name

	def save(
			self, force_insert=False, force_update=False, using=None, update_fields=None
	):
		if self.is_active:
			SiteSettingModel.objects.filter(is_active=True).update(is_active=False)
		self.site_url = slugify(self.site_name)
		return super(SiteSettingModel, self).save()