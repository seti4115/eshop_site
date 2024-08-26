from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from user_module.models import UserModel
from . import models
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .forms import CommentForm


class ProductListView(ListView):
	model = models.ProductModel
	template_name = 'home_module/index.html'
	paginate_by = 3

	def get_queryset(self):
		base = super(ProductListView, self).get_queryset()
		return base

	def get_context_data(self, *, object_list=None, offer=None, **kwargs):
		context = super(ProductListView, self).get_context_data()
		context['new_offer'] = self.get_queryset().filter(new_offer=True).order_by('-id')[:4]
		context['page_obj'] = self.get_queryset()
		context['user'] = UserModel.objects.all()
		return context


class CommentGet(DetailView):
	model = models.ProductModel
	template_name = 'product_module/single.html'
	slug_field = 'urlname'
	slug_url_kwarg = 'slug'

	def get_context_data(self, **kwargs):  # new
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
		self.object = self.get_object()
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):
		comment = form.save(commit=False)
		comment.product = self.object
		comment.user = self.request.user
		comment.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('product-detail-page', kwargs={'slug': self.object.urlname})


class ProductDetailView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		if request.user.is_superuser:
			view = CommentGet.as_view()
		else:
			view = CommentGet.as_view()
		return view(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		view = CommentPost.as_view()
		return view(request, *args, **kwargs)


class ProductAddView(LoginRequiredMixin, CreateView):
	model = models.ProductModel
	template_name = 'product_module/addProduct.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('product-detail-page', kwargs={'slug': self.object.urlname})


class ProductEditeView(LoginRequiredMixin, UpdateView):
	model = models.ProductModel
	template_name = 'product_module/editProduct.html'
	fields = ["title", "price"]
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