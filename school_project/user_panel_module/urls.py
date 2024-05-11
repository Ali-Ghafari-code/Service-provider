from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel'),
    path('servicer/', views.ServicerPanelDashboardPage.as_view(), name='servicer_panel'),
    path('servicer/service-submit/', views.UserServiceSubmit.as_view(), name='user_service_submit'),
    path('user/service-request/', views.UserServiceRequest.as_view(), name='user_service_request'),
    path('edit-profile/', views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('edit-servicer-profile/', views.EditServicerProfilePage.as_view(), name='edit_servicer_page'),
]
