from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from account_module.models import Servicer
from user_panel_module.forms import UserProfileForm, ServicerProfileForm
from user_request_module.forms import ServiceForm


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
        add = request.user.address
        if service_form.is_valid():
            print('reques' ,add)
            service_form.save(commit=True)

            return redirect('home_page')
        else:
            print('reques' ,add)
            context ={
                'form': service_form
            }
            return render(request, 'user_request_module/user_request_page.html', context)
