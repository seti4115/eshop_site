from django.db import models

# Create your models here.


class SliderModel(models.Model):
	name = models.CharField(max_length=150)
	short_description = models.TextField()
	image = models.ImageField(upload_to='images/')
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.name