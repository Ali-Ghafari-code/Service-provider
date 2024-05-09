from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserRequestPage.as_view(), name='user-request'),
    path('requests', views.RequestsPage.as_view(), name='requests'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='Service_detail'),
]
