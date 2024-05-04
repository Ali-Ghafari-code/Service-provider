from django.contrib import admin
from account_module import models
from account_module.models import User


# Register your models here.


admin.site.register(models.User)
