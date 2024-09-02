from django.shortcuts import render
from django.views.generic.base import TemplateView
from site_settings.models import SiteSettingModel
from user_module.models import CommentModel


class header_partial(TemplateView):
    template_name = 'header-partial.html'

    def get_context_data(self, **kwargs):
        context = super(header_partial, self).get_context_data()
        context['site'] = SiteSettingModel.objects.filter(is_active=True).first()
        return context


class footer_partial(TemplateView):
    template_name = 'footer-partial.html'

    def get_context_data(self, **kwargs):
        context = super(footer_partial, self).get_context_data()
        context['site'] = SiteSettingModel.objects.filter(is_active=True).first()
        return context


def error404(request):
    return render(request, '404.html')


class AboutView(TemplateView):
    template_name = 'home_module/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        context['site'] = SiteSettingModel.objects.filter(is_active=True).first()
        context['comments'] = CommentModel.objects.filter(is_best=True)
        return context


class FAQView(TemplateView):
    template_name = 'home_module/faq.html'