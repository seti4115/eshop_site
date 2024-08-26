from django.urls import path
from . import views


urlpatterns = [
    path('login-', views.LoginView.as_view(), name='login-page'),
    path('register-', views.RegisterView.as_view(), name='register-page'),
    # path('contact-', views.ContactView.as_view(), name = 'contact-page'),
    path('logout-', views.LogoutView.as_view(), name='logout-page')

]