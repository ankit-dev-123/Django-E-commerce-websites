from django.urls import path
from .views import *

# URL patterns for the shopping cart application
urlpatterns = [
    path("", cart, name="cart"),
    path("add-to-cart/<slug:slug>/", add_to_cart, name="add_to_cart"),
    path("increase-quantity/<int:id>/", increase_quantity, name="increase_quantity"),
    path("decrease-quantity/<int:id>/", decrease_quantity, name="decrease_quantity"),
    path("remove-cart-item/<int:id>/", remove_cart_item, name="remove_cart_item"),
    path("payment-success/", payment_success, name="payment_success"),
]