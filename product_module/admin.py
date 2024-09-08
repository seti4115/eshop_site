from django.contrib import admin
from django.utils.html import format_html

from . import models


@admin.action(description='delete')
def delete(modeladmin, request, queryset):
	for a in queryset:
		a.delete()


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price_discount', 'urlname', 'id', 'new_offer')
	list_editable = ['new_offer']
	ordering = ['-id']


class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'is_active']
	list_editable = ['is_active']


admin.site.register(models.ProductModel, ProductAdmin)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
