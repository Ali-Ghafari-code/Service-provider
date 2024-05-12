from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, DetailView
from account_module.models import User
from account_module.models import Servicer
from payment_module.models import Payment
from user_panel_module.forms import UserProfileForm, ServicerProfileForm
from user_request_module.models import Service


# from .forms import UserProfileForm


# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user/user_panel.html'


@method_decorator(login_required, name='dispatch')
class ServicerPanelDashboardPage(TemplateView):
    template_name = 'servicer/user_panel.html'


@method_decorator(login_required, name='dispatch')
class UserServiceSubmit(View):
    def get(self, request):
        current_servicer = Servicer.objects.filter(user=request.user).first()
        context = Service.objects.filter(servicer=current_servicer).get()
        context_2 = Payment.objects.filter(service=context.id).first()
        context = {
            'context': context,
            'pay': context_2,
        }
        return render(request, 'servicer/user_service_submit.html', context)


@method_decorator(login_required, name='dispatch')
class UserServiceRequest(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        context = Service.objects.filter(user=current_user).all()
        context = {
            'context': context
        }
        return render(request, 'user/user_service_request.html', context)


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = UserProfileForm(instance=current_user)
        context = {
            'form': edit_form
        }
        return render(request, 'user/edit_user_profile.html', context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = UserProfileForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form
        }
        return render(request, 'user/edit_user_profile.html', context)


@method_decorator(login_required, name='dispatch')
class EditServicerProfilePage(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form_user = UserProfileForm(instance=current_user)
        current_servicer = Servicer.objects.filter(user=request.user).first()
        edit_form = ServicerProfileForm(instance=current_servicer)
        context = {
            'servicer': edit_form,
            'user': edit_form_user
        }
        return render(request, 'servicer/edit_user_profile.html', context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form_user = UserProfileForm(request.POST, request.FILES, instance=current_user)
        current_servicer = Servicer.objects.filter(user=request.user).first()
        edit_form_servicer = ServicerProfileForm(request.POST, request.FILES, instance=current_servicer)

        if edit_form_user.is_valid() and edit_form_servicer.is_valid():
            edit_form_user.save(commit=True)
            edit_form_servicer.save(commit=True)
            servicer = Servicer.objects.filter(user=request.user).first()
            if servicer:
                request.session['servicer_info'] = {
                    'gender': servicer.gender,
                    'certificate': servicer.certificate,
                    'experience': servicer.experience,
                    'description': servicer.description
                }

        context = {
            'servicer': edit_form_servicer,
            'user': edit_form_user
        }
        return render(request, 'servicer/edit_user_profile.html', context)


def servicer_panel_header(request: HttpRequest):
    return render(request, 'servicer/shared/header_profile.html')


def user_panel_header(request: HttpRequest):
    return render(request, 'user/shared/header_profile.html')
