from django.contrib import admin
from . import models
from product_module import models

# Register your models here.


class CommentInline(admin.StackedInline):
    model = models.CommentModel
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    inlines = [
        CommentInline,
    ]


admin.site.register(models.UserModel, UserAdmin)
admin.site.register(models.CommentModel)