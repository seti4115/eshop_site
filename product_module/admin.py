from django.contrib import admin
from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	list_display = ['title', 'price_discount', 'urlname', 'id']
	ordering = ['-id']


admin.site.register(models.ProductModel, ProductAdmin)