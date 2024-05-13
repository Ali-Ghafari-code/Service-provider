from django.contrib import admin

# Register your models here.
from user_panel_module import models

admin.site.register(models.Comment)