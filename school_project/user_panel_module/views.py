from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from account_module.models import Servicer
# from .forms import UserProfileForm


# Create your views here.
class UserPanelDashboardPage(TemplateView):
    template_name = 'user/user_panel.html'


class ServicerPanelDashboardPage(TemplateView):
    template_name = 'servicer/user_panel.html'


class EditUserProfilePage(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = UserProfileForm(instance=current_user)
        context = {
            'form': edit_form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = UserProfileForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)

        context = {
            'form': edit_form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


# def user_panel_menu_partial(request: HttpRequest):
#     return render(request, 'user_panel_module/partials/user_panel_menu_partial.html')
#
#
