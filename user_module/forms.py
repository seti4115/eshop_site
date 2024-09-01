from tkinter.tix import Form
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserModel
from . import models


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-form-grids', 'placeholder': 'password', 'type': 'password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        user = UserModel(
            email=email, username=username
        )
        if password == confirm_password:
            user.set_password(password)


class LoginForm(forms.ModelForm):

    class Meta:
        model = models.UserModel
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'login-form-grids', 'placeholder': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'login-form-grids', 'placeholder': 'password'})
        }


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)


class ResetPasswordForm(forms.Form):
    new_pass = forms.CharField(widget=forms.PasswordInput)
    confirm_new_pass = forms.CharField(widget=forms.PasswordInput)