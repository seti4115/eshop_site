from django.urls import path
from . import views


urlpatterns = [
    path('login-', views.LoginView.as_view(), name='login-page'),
    path('register-', views.RegisterView.as_view(), name='register-page'),
    path('forgot-password', views.ForgotPasswordView.as_view(), name='forgot_pass-page'),
    path('active-account/<active_code>', views.ActiveAccountView.as_view(), name='active-account-page'),
    path('reset-password/<active_code>', views.ResetPasswordView.as_view(), name='reset_pass-page'),
    path('contact-', views.ContactView.as_view(), name='contact-page'),
    path('logout-', views.LogoutView.as_view(), name='logout-page'),



]