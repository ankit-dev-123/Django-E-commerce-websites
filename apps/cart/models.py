from django.db import models
from apps.products.models import Product

# Model to represent a single item in the user's shopping cart
class Cart(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Method to calculate the total price for this specific cart item (unit price * quantity)
    def get_total_price(self):
        return self.product.price * self.quantity

    # String representation of the cart item for the admin panel and debugging
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
