from django.urls import path
from . import views

urlpatterns = [
	path('', views.ProductListView.as_view(), name='home-page'),
	path('add-/', views.ProductAddView.as_view(), name='add-page'),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail-page'),
	path('<slug:slug>/edit-/', views.ProductEditeView.as_view(), name='edit-product-page'),
	path('<slug:slug>/delete-/', views.ProductDeleteView.as_view(), name='delete-product-page'),
]