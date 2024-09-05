from django.contrib import admin
from django.utils.html import format_html

from . import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):

	list_display = ('title', 'price_discount', 'urlname', 'id',)
	ordering = ['-id']

	def save_model(self, request, obj, form, change):
		if not change:
			obj.author = request.user
			obj.save()
		return super(ProductAdmin, self).save_model()


admin.site.register(models.ProductModel, ProductAdmin)