from .models import Cart
from apps.products.models import Product
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
from decimal import Decimal

# View to add a product to the user's shopping cart
@login_required
def add_to_cart(request, slug):
    # Fetch the product using its unique slug
    product = Product.objects.get(slug=slug)
    # Extracts quantity from the GET parameters, defaulting to 1 if not provided or invalid
    try:
        qty = int(request.GET.get('quantity', 1))
    except ValueError:
        qty = 1

    # Get the existing cart item or create a new one for the current user and product
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )
    
    # If the item already existed, increment its quantity; otherwise, set it to the requested qty
    if not created:
        cart_item.quantity += qty
    else:
        cart_item.quantity = qty
        
    cart_item.save()
    
    # Redirect back to the previous page (referer) or to the cart page
    referer = request.META.get('HTTP_REFERER')
    if referer and 'login' not in referer:
        return redirect(referer)
    return redirect('cart')

# View to display the contents of the cart and calculate totals/taxes
@login_required
def cart(request):
    # Retrieve all cart items belonging to the logged-in user
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0

    # Calculate the total price of all items in the cart
    for item in cart_items:
        total_price += item.product.price * item.quantity

    # Calculate a 2% tax on the total price
    tax = total_price * Decimal('0.02')
    grand_total = total_price + tax
    
    # Convert total price to paise (the smallest currency unit) for Razorpay
    amount = int(total_price * 100)

    payment = None
    # If there is an amount to pay, create a Razorpay order
    if amount > 0:
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1"
        })
    
    # Context dictionary to pass all cart and payment data to the template
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "tax": tax,
        "grand_total": grand_total,
        "payment": payment,
        "razorpay_key": settings.RAZORPAY_KEY_ID
    }
    return render(request, "cart/cart.html", context)

# View called after a successful payment to clear the user's cart
@login_required
def payment_success(request):
    # Deletes all cart items for the user after payment completion
    Cart.objects.filter(user=request.user).delete()
    return redirect('products')

# View to increment the quantity of a specific cart item
@login_required
def increase_quantity(request, id):
    item = Cart.objects.get(id=id)
    item.quantity += 1
    item.save()
    return redirect('cart')

# View to decrement the quantity of a specific cart item
@login_required
def decrease_quantity(request, id):
    item = Cart.objects.get(id=id)
    item.quantity -= 1
    item.save()
    return redirect('cart')

# View to completely remove an item from the shopping cart
@login_required
def remove_cart_item(request, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('cart')