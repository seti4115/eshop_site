from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
from django.utils.text import slugify


class ProductModel(models.Model):
	title = models.CharField(max_length=150, unique=True)
	rating = models.PositiveIntegerField(
		validators=[MaxValueValidator(limit_value=5), MinValueValidator(limit_value=1)])
	price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField(
		validators=[MaxValueValidator(limit_value=100), MinValueValidator(limit_value=0)])
	price_discount = models.FloatField(editable=False)
	urlname = models.SlugField(editable=False, allow_unicode=True, unique=True)
	image = models.ImageField(upload_to='images', null=True, blank=True)
	new_offer = models.BooleanField(default=False)

	def save(
			self, *args, **kwargs
	):
		self.price_discount = self.price - ((self.price * self.discount) / 100)
		self.urlname = slugify(self.title)
		return super(ProductModel, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_discount(self):
		discount = ((self.price * self.discount) / 100)
		return discount

