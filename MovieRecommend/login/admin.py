from django.contrib import admin
from . import models
from .models import Users

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'Username', "Password")


admin.site.register(models.Users,UserAdmin)
