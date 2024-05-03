from django.contrib import admin

# Register your models here.
from new_app import models

admin.site.register(models.Todo)
admin.site.register(models.Todont)