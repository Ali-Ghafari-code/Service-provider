from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from jalali_date import date2jalali

from account_module.models import User, Servicer
from payment_module.models import Payment


# Create your models here.
from user_request_module.models import Service


class Comment(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='comment_by_user')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    servicer = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='comment_by_servicer')
    comment = models.TextField(verbose_name='نظر کاربر', max_length=300)
