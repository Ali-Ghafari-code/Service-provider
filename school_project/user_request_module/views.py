from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from jalali_date import datetime2jalali, date2jalali
from account_module.models import User
from account_module.models import Servicer
from user_request_module.forms import ServiceForm, Servicertypeform
from user_request_module.models import Service


# from .forms import UserProfileForm


# Create your views here.
class ServicerTypePage(View):
    def get(self, request):
        edit_form = Servicertypeform()
        context = {
            'form': edit_form
        }
        return render(request, 'servicer_type_module/servicer_type_page.html', context)

    def post(self, request):
        current_servicer = Servicer.objects.filter(user=request.user).first()
        edit_form_servicer = Servicertypeform(request.POST, request.FILES, instance=current_servicer)
        if edit_form_servicer.is_valid():
            edit_form_servicer.save(commit=True)
            servicer = Servicer.objects.filter(user=request.user).first()
            if servicer:
                request.session['servicer_info'] = {
                    'gender': servicer.gender,
                    'certificate': servicer.certificate,
                    'experience': servicer.experience,
                    'description': servicer.description
                }
            return redirect('servicer_panel')
        context = {
            'form': edit_form_servicer
        }
        return render(request, 'servicer_type_module/servicer_type_page.html', context)


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
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        # فیلتر کردن اشیاء بر اساس مقدار is_submit
        context = queryset.filter(is_submit=False)
        return context


class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
