from django.urls import path
from .views import products, single_product

# URL patterns for the products app
urlpatterns = [
    # URL for the main products listing page
    path('', products, name='products'),
    # URL for a single product detail page, identified by its slug
    path('single-product/<slug:slug>/', single_product, name='single-product')
]