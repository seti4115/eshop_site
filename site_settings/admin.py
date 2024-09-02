from django.contrib import admin

# Register your models here.
from site_settings.models import SiteSettingModel

admin.site.register(SiteSettingModel)