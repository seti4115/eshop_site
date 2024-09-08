
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from slider.models import SliderModel
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .forms import CommentForm



class ProductListView(ListView):
	model = models.ProductModel
	template_name = 'home_module/index.html'
	paginate_by = 3

	def get_queryset(self):
		base = super(ProductListView, self).get_queryset().order_by('id')
		return base

	def get_context_data(self, *, object_list=None, offer=None, **kwargs):
		context = super(ProductListView, self).get_context_data()
		context['new_offer'] = self.get_queryset().filter(new_offer=True).order_by('-id')[:4]
		context['sliders'] = SliderModel.objects.filter(is_active=True)
		return context


class GetDetailView(DetailView):
	model = models.ProductModel
	template_name = 'product_module/single.html'
	slug_field = 'urlname'
	slug_url_kwarg = 'slug'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = CommentForm()
		return context


class CommentPost(SingleObjectMixin, FormView):
	model = models.ProductModel
	form_class = CommentForm
	template_name = "product_module/single.html"
	slug_field = 'urlname'
	slug_url_kwarg = 'slug'

	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			self.object = self.get_object()
			return super().post(request, *args, **kwargs)
		return render(request, 'loginRequired.html')

	def form_valid(self, form):
		comment = form.save(commit=False)
		comment.product = self.object
		comment.user = self.request.user
		comment.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('product-detail-page', kwargs={'slug': self.object.urlname})


class ProductDetailView(View):

	def get(self, request: HttpRequest, *args, **kwargs):
		view = GetDetailView.as_view()
		return view(request, *args, **kwargs)

	def post(self, request: HttpRequest, *args, **kwargs):
		view = CommentPost.as_view()
		return view(request, *args, **kwargs)


class ProductAddView(LoginRequiredMixin, CreateView):
	model = models.ProductModel
	template_name = 'product_module/addProduct.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('product-detail-page', kwargs={'slug': self.object.urlname})

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ProductEditeView(LoginRequiredMixin, UpdateView):
	model = models.ProductModel
	template_name = 'product_module/editProduct.html'
	fields = ["title", "price", 'image', 'new_offer', 'description', 'selected_categories']
	slug_field = 'urlname'
	slug_url_kwarg = 'slug'

	def get_success_url(self):
		return reverse_lazy('product-detail-page', kwargs={'slug': self.object.urlname})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
	model = models.ProductModel
	template_name = 'product_module/deleteProduct.html'
	success_url = reverse_lazy("home-page")
	slug_field = 'urlname'
	slug_url_kwarg = 'slug'


class ProductCategoryView(ListView):
	model = models.ProductModel
	template_name = 'product_module/categorylist.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductCategoryView, self).get_context_data(*args, **kwargs)
		return context

	def get_queryset(self):
		query = super(ProductCategoryView, self).get_queryset()
		category_name = self.kwargs.get('category')
		if category_name is not None:
			query = query.filter(Q(selected_categories__url_title__iexact=category_name))
		return query