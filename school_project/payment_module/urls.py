from django.urls import path
from . import views

urlpatterns = [
    path('', views.PayService.as_view(), name='payment_page'),
]
