from django.urls import path
from . import views


urlpatterns = [
	path('error404-', views.error404, name='not-found-page'),
	path('about-', views.AboutView.as_view(), name='about-page'),
	path('FAQ-', views.FAQView.as_view(), name='faq-page'),
]

