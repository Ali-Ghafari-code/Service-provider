from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from account_module.models import User
from account_module.models import Servicer
from user_request_module.forms import ServiceForm, Servicertypeform
from user_request_module.models import Service


# Create your views here.


class SubmitServiceView(View):
    def get(self, request, service_id):
        service = get_object_or_404(Service, pk=service_id)
        service.is_submit = True
        servicer = get_object_or_404(Servicer, user=request.user)
        service.servicer = servicer
        if servicer.is_submited:
            service.save()
            return redirect('user_service_submit')
        else:
            messages.error(request, "اطلاعات شما توسط ادمین پذیرفته نشده است.")
            return redirect('servicer_panel')

    def post(self, request, *args, **kwargs):
        pass


class DeleteServiceView(View):
    def get(self, request, *args, **kwargs):
        service_id = self.kwargs.get('service_id')
        service = get_object_or_404(Service, pk=service_id)
        if service.user == request.user:
            service.delete()
            return redirect('user_service_request')
        else:
            messages.error(request, "شما مجاز به حذف این سرویس نیستید.")
            return redirect('servicer_panel')
