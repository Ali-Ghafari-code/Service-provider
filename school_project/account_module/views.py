from django.http import Http404
from django.urls import reverse
from django.contrib.auth import login, logout
# from .models import User
from django.shortcuts import render, redirect
from django.views import View
from django.utils.crypto import get_random_string
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User, Servicer
from account_module.forms import RegisterForm


# from utils.email_service import send_email

# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            fullname = register_form.cleaned_data.get('fullname')
            user_password = register_form.cleaned_data.get('password')
            is_servicer = register_form.cleaned_data.get('user_type')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                if is_servicer == "servicer":
                    new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False,
                                    username=user_email, fullname=fullname, is_servicer=True)
                    new_user.set_password(user_password)
                    new_user.save()
                    new_servicer = Servicer(user=new_user)
                    new_servicer.save()
                    return redirect('login_page')
                else:
                    new_user = User(email=user_email, email_active_code=get_random_string(72), is_active=False,
                                    username=user_email, fullname=fullname)
                    new_user.set_password(user_password)
                    new_user.save()
                    # send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/active_account.html')
                    return redirect('login_page')

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=user_email).first()

            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است.')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        if user.is_servicer:
                            servicer = Servicer.objects.filter(
                                user=user).first()  # Filter based on the user object, not email
                            if servicer:
                                request.session['servicer_info'] = {
                                    'gender': servicer.gender,
                                    'certificate': servicer.certificate,
                                    'type': servicer.type,
                                    'is_submited': servicer.is_submited,
                                    'experience': servicer.experience,
                                    'description': servicer.description
                                }
                                return redirect(reverse('servicer_panel'))
                            else:
                                return redirect(reverse('user_panel'))
                        else:
                            return redirect(reverse('user_panel'))
                    else:
                        login_form.add_error('email', 'نام کاربری و یا کلمه ی عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده پیدا نشد.')

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


#
# class ActivateAccountView(View):
#     def get(self, request, email_active_code):
#         user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
#         if user is not None:
#             if not user.is_active:
#                 user.is_active = True
#                 user.email_active_code = get_random_string(72)
#                 user.save()
#                 return redirect(reverse('login_page'))
#             else:
#                 pass
#
#         raise Http404
#
#
# class ForgetPassword(View):
#     def get(self, request):
#         forget_pass_form = ForgotPasswordForm()
#         context = {'forget_pass_form': forget_pass_form}
#         return render(request, 'account_module/forgot_password.html', context)
#
#     def post(self, request):
#         forget_pass_form = ForgotPasswordForm(request.POST)
#         if forget_pass_form.is_valid():
#             user_email = forget_pass_form.cleaned_data.get('email')
#             user = User.objects.filter(email__iexact=user_email).first()
#             if user is not None:
#                 send_email('بازیابی کلمه ی عبور', user.email, {'user': user}, 'emails/forgot_password.html')
#                 return redirect(reverse('home_page'))
#
#         context = {'forget_pass_form': forget_pass_form}
#         return render(request, 'account_module/forgot_password.html', context)
#
#
# class ResetPassword(View):
#     def get(self, request, active_code):
#         user = User.objects.filter(email_active_code__iexact=active_code).first()
#         if user is None:
#             return redirect(reverse('login_page'))
#
#         reset_pass_form = ResetPasswordForm()
#         context = {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         }
#         return render(request, 'account_module/reset_password.html', context)
#
#     def post(self, request, active_code):
#         reset_pass_form = ResetPasswordForm(request.POST)
#         user = User.objects.filter(email_active_code__iexact=active_code).first()
#         if reset_pass_form.is_valid():
#             if user is None:
#                 return redirect(reverse('login_page'))
#             user_new_password = reset_pass_form.cleaned_data.get('password')
#             user.set_password(user_new_password)
#             user.email_active_code = get_random_string(72)
#             user.is_active = True
#             user.save()
#             return redirect(reverse('login_page'))
#         context = {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         }
#         return render(request, 'account_module/reset_password.html', context)
#
#
class LogoutView(View):
    def get(self, request):
        # Clear session variables related to being a servicer
        if 'servicer_info' in request.session:
            del request.session['servicer_info']

        # Logout the user
        logout(request)

        # Redirect to the login page after logout
        return redirect(reverse('login_page'))
