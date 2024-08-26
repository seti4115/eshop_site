from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView


def header_partial(request):
    return render(request, 'header-partial.html')


def footer_partial(request):
    return render(request, 'footer-partial.html')


def error404(request):
    return render(request, '404.html')

