from django.urls import path
from . import views


urlpatterns = [
	path('error404-', views.error404, name='not-found-page')
]

