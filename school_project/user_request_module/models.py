from django.db import models
from account_module.models import User, Servicer


# Create your models here.

class Service(models.Model):
    servicer = models.ForeignKey(Servicer, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=300, db_index=True, verbose_name='نوع خدمات')
    gender = models.CharField(max_length=10, verbose_name='جنسیت خدمات دهنده', blank=True)
    description = models.TextField(db_index=True, verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='هزینه', blank=True, null=True)
    slug = models.SlugField(default="", null=True, blank=True, max_length=200, unique=True)
    service_date = models.DateTimeField(verbose_name='تاریخ انجام پروژه')
    address = models.TextField(db_index=True, verbose_name='محل انجام خدمات')
    service_time = models.IntegerField(verbose_name='ساعت خدمت')
    is_submit = models.BooleanField(default=False, verbose_name='قبول شده / نشده')


