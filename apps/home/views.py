from django.shortcuts import render
from apps.products.models import Product, Category

# View to render the main landing page of the application
def home(request):
    # Fetch all products from the database to display on the home page
    products_list = Product.objects.all()
    # Context dictionary to pass product data to the template
    context = {
        'products' : products_list,
    }
    return render(request, 'home/index.html', context)
