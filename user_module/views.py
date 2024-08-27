from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login, logout

from first import settings
from . import forms, models


# Create your views here.

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
                    email_active_code=get_random_string(128),
                    is_active=False,
                    username=username)
                new_user.set_password(user_password)
                new_user.save()
                subject = 'welcome to GFG world'
                message = f'Hi {new_user.username}, thank you for registering in geeksforgeeks.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [new_user.email, ]
                send_mail(subject, message, email_from, recipient_list)
                # todo: send email active code
                return redirect(reverse('login-page'))

        context = {
            'form': form
        }

        return render(request, 'user_module/registered.html', context)