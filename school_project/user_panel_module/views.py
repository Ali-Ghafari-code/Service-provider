from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, DetailView
from account_module.models import User
from account_module.models import Servicer
from payment_module.models import Payment
from user_panel_module.forms import UserProfileForm, ServicerProfileForm, CommentForm
from user_panel_module.models import Comment
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
        context = Service.objects.filter(servicer=current_servicer).first()
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
        for service in context:
            payment = Payment.objects.filter(service=service).first()

        context = {
            'context': context,
            'pay': payment,
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


class ServiceComment(View):
    def get(self, request, service_id):
        comment_form = CommentForm(
            initial={'service_id': service_id})  # افزودن service_id به فرم به عنوان مقدار پیشفرض فیلد پنهان
        context = {
            'comment': comment_form,
        }
        return render(request, 'user/user_comment.html', context)


class DeleteServiceView(View):
    def get(self, request, service_id, *args, **kwargs):
        service = Service.objects.get(id=service_id)
        service.delete()
        messages.success(request, "پایان خدمات با موفقیت انجام شد")
        return redirect('servicer_panel')


class ServiceCommentSave(View):
    def post(self, request):
        service_id = request.POST.get('service_id')
        comment_text = request.POST.get('comment')
        user = request.user

        comment = Comment.objects.create(
            service_id=service_id,
            user=user,
            servicer=Service.objects.get(id=service_id),
            comment=comment_text
        )
        comment.service.comment = comment
        comment.service.save()
        return redirect('user_service_request')


class ServicerComment(View):
    def get(self, request):
        servicer = get_object_or_404(Servicer, user=request.user)

        services = Service.objects.filter(servicer=servicer).all()

        servicer_comments = Comment.objects.filter(service__in=services).all()

        context = {
            'servicer_comments': servicer_comments
        }
        return render(request, 'servicer/user_panel_works_comment.html', context)


def servicer_panel_header(request):
    service = Service.objects.filter(servicer=request.user.servicer)
    return render(request, 'servicer/shared/header_profile.html', {'service': service})


def user_panel_header(request: HttpRequest):
    return render(request, 'user/shared/header_profile.html')
