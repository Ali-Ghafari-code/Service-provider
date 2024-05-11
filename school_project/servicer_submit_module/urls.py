from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:service_id>/', views.SubmitServiceView.as_view(), name='service-submit'),
    path('delete/<int:service_id>/', views.DeleteServiceView.as_view(), name='Service_delete'),

]