from .models import Cart

def cart_items_count(request):
    if request.user.is_authenticated:
        # User ke cart mein kitne unique products hain unka count
        count = Cart.objects.filter(user=request.user).count()
    else:
        count = 0
    return {'cart_items_count': count}
