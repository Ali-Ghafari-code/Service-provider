from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserRequestPage.as_view(), name='user-request'),
]
