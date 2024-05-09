from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from jalali_date import datetime2jalali, date2jalali
from account_module.models import User
from account_module.models import Servicer
from user_request_module.forms import ServiceForm
from user_request_module.models import Service


# from .forms import UserProfileForm


# Create your views here.
class UserRequestPage(View):
    def get(self, request):
        edit_form = ServiceForm()
        context = {
            'form': edit_form
        }
        return render(request, 'user_request_module/user_request_page.html', context)

    def post(self, request):
        service_form = ServiceForm(request.POST)
        user = request.user
        if user.address and user.mobile_number and user.city is not None:
            if service_form.is_valid():
                service_type = service_form.cleaned_data.get('type')
                service_date = service_form.cleaned_data.get('service_date')
                gender = service_form.cleaned_data.get('gender')
                price = service_form.cleaned_data.get('price')
                service_time = service_form.cleaned_data.get('service_time')
                description = service_form.cleaned_data.get('description')

                new_service = Service(type=service_type, service_date=service_date, gender=gender,price=price,
                                      service_time=service_time, description=description, user=user)
                new_service.save()
                return redirect('requests')
            context = {
                'form': service_form
            }
            return render(request, 'user_request_module/user_request_page.html', context)
        else:
            context = {
                'form': service_form,
                'error_message': 'اطلاعات کاربری شما کامل نیستند. لطفاً اطلاعات خود را تکمیل کنید.'
            }
            return render(request, 'user_request_module/user_request_page.html', context)


class RequestsPage(ListView):
    model = Service
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
