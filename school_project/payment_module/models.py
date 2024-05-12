from django.db import models


# Create your models here.
class Payment(models.Model):
    service = models.OneToOneField('user_request_module.Service', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='مبلغ پرداخت')
    success = models.BooleanField(verbose_name='پرداخت شده ؟', default=False)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان پرداخت')
