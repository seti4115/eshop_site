from django.contrib import admin

# Register your models here.
from site_settings.models import SiteSettingModel


class SiteAdmin(admin.ModelAdmin):
	list_display = ['site_name', 'is_active']
	list_editable = ['is_active']


admin.site.register(SiteSettingModel, SiteAdmin)