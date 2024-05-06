from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(max_length=20, verbose_name='تصویر پروفایل', null=True, blank=True)
    fullname = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    city = models.CharField(max_length=100, verbose_name='استان و شهر', blank=True, null=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    national_number = models.IntegerField(null=True, blank=True, verbose_name='شماره ملی')
    mobile_number = models.IntegerField(null=True, blank=True, verbose_name='شماره موبایل')
    birth_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ تولد')
    is_servicer = models.CharField(max_length=100, verbose_name='خدمات دهنده', default=False)


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_username()


class Servicer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='servicer')
    gender = models.CharField(max_length=100, verbose_name='جنسیت')
    certificate = models.CharField(max_length=100, verbose_name='مدارک تحصیلی')
    type = models.CharField(max_length=100, verbose_name='نوع خدمات رسانی')
    is_submited = models.BooleanField(verbose_name='تایید شده', default=False)
    experience = models.IntegerField(null=True, blank=True, verbose_name='سال تجربه')
    description = models.CharField(max_length=300, verbose_name='توضیحات')


    class Meta:
        verbose_name = 'خدمات دهنده'
        verbose_name_plural = 'خدمات دهندگان'
