from django.core.mail import EmailMessage
from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login, logout

from first import settings
from . import forms, models


# Create your views here.
from .forms import ForgotPasswordForm, ResetPasswordForm
from .models import UserModel


class LoginView(FormView):
    template_name = 'user_module/login.html'
    form_class = forms.LoginForm

    def post(self, request, *args, **kwargs):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user: models.UserModel = models.UserModel.objects.filter(email__iexact=email).first()
            if user is not None:
                is_password_correct = user.check_password(password)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home-page'))
                else:
                    login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'user_module/logout.html')


class RegisterView(View):

    def get(self, request):
        form = forms.RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'user_module/registered.html', context)

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email')
            user_password = form.cleaned_data.get('password')
            user: bool = models.UserModel.objects.filter(email__iexact=user_email).exists()
            if user:
                form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = models.UserModel(
                    email=user_email,
                    is_active=False,
                    username=username,
                    email_active_code=get_random_string(128)
                    )
                new_user.set_password(user_password)
                new_user.save()
                subject = 'welcome to GFG world'
                message = f'Hi {new_user.username}, thank you for registering in geeksforgeeks.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [new_user.email, ]
                email = EmailMessage(subject, message, email_from, recipient_list)
                email.send()
                # todo: send email active code
                return redirect(reverse('login-page'))

        context = {
            'form': form
        }

        return render(request, 'user_module/registered.html', context)


class ContactView(TemplateView):
    template_name = 'user_module/contact.html'


class ActiveAccountView(View):

    def get(self, request: HttpRequest, active_code):
        user: UserModel = UserModel.objects.filter(email_active_code__iexact=active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(128)
                user.save()
                # todo: show success message to user
                return render(request, 'user_module/active_account.html')
            else:
                # todo: show your account was activated message to user
                pass

        return redirect(reverse('not-found-page'))


class ForgotPasswordView(View):

    def get(self, request, *args, **kwargs):
        forgot_pass_form = ForgotPasswordForm()
        return render(request, 'user_module/forgot_pass.html', {
            'forgot_pass_form': forgot_pass_form,
        })

    def post(self, request, *args, **kwargs):
        forgot_pass_form = ForgotPasswordForm(request.POST)
        if forgot_pass_form.is_valid():
            user_email = forgot_pass_form.cleaned_data.get('email')
            user = UserModel.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # todo: send email
                pass
            return redirect(reverse('login-page'))

        context = {'forget_pass_form': forgot_pass_form}
        return render(request, 'user_module/forgot_pass.html', context)


class ResetPasswordView(View):

    def get(self, request: HttpRequest, active_code):
        user: UserModel = UserModel.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login-page'))

        reset_pass_form = ResetPasswordForm()

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'user_module/reset_pass.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: UserModel = UserModel.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('login-page'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(128)
            user.is_active = True
            user.save()
            return redirect(reverse('login-page'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'user_module/reset_pass.html', context)


class ProfileView(View):
    def get(self, request:HttpRequest, *args, **kwargs):
        return render(request, 'user_module/profile.html')