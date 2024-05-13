from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from jalali_date import date2jalali
# from user_panel_module.models import Comment
from account_module.models import User, Servicer
from payment_module.models import Payment


# Create your models here.


class Service(models.Model):
    serviceid = models.IntegerField(auto_created=True, null=True)
    servicer = models.ForeignKey(Servicer, blank=True, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=500, verbose_name='نوع خدمات')
    gender = models.CharField(max_length=100, verbose_name='جنسیت خدمات دهنده', blank=True)
    description = models.TextField(db_index=True, verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='هزینه', blank=True, null=True)
    service_date = models.CharField(max_length=100, verbose_name='تاریخ انجام پروژه')
    service_time = models.IntegerField(verbose_name='ساعت خدمت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساعت خدمت')
    is_submit = models.BooleanField(default=False, verbose_name='قبول شده / نشده')
    pay = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='related_service_payment')
    comment = models.OneToOneField('user_panel_module.Comment', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='related_service_comment')


