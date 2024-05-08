from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from account_module.models import Servicer
from user_panel_module.forms import UserProfileForm, ServicerProfileForm


# from .forms import UserProfileForm


# Create your views here.
class UserRequestPage(View):
    def get(self, request):
        # current_user = User.objects.filter(id=request.user.id).first()
        # edit_form = UserProfileForm(instance=current_user)
        # context = {
        #     'form': edit_form
        # }
        return render(request, 'user_request_module/user_request_page.html', {})

    # def post(self, request):
    #     current_user = User.objects.filter(id=request.user.id).first()
    #     edit_form = UserProfileForm(request.POST, request.FILES, instance=current_user)
    #     if edit_form.is_valid():
    #         edit_form.save(commit=True)
    #
    #     context = {
    #         'form': edit_form
    #     }
    #     return render(request, 'user/edit_user_profile.html', context)
