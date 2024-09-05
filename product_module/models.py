from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from sorl.thumbnail import ImageField
from first import settings
from user_module.models import UserModel


class ProductModel(models.Model):
	title = models.CharField(max_length=150, unique=True)
	rating = models.PositiveIntegerField(
		validators=[MaxValueValidator(limit_value=5), MinValueValidator(limit_value=1)])
	price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField(
		validators=[MaxValueValidator(limit_value=100), MinValueValidator(limit_value=0)])
	price_discount = models.FloatField(editable=False)
	urlname = models.SlugField(editable=False, allow_unicode=True, unique=True)
	image = ImageField(upload_to='images', null=True, blank=True)
	new_offer = models.BooleanField(default=False)
	author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, editable=False)

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


class CommentModel(models.Model):
	product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
	comment = models.TextField()
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)
	is_best = models.BooleanField(default=False)

	def __str__(self):
		return self.comment

	def get_absolute_url(self):
		return reverse("home-page")
