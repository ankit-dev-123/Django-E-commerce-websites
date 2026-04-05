from django.shortcuts import render, get_object_or_404
from .models import Product, SubCategory, Brand, SizeVariant, ColorVariant
from django.core.paginator import Paginator
from django.db.models import Q

# View to list all products with filtering, search, and pagination
def products(request):
    products_list = Product.objects.all() # Fetch all products initially
    # Extract filter parameters from the GET request
    search = request.GET.get('search')
    category = request.GET.get('category')
    sub_category = request.GET.get('subCategory')
    brand = request.GET.get('brand')
    price_min = request.GET.get('priceMin')

    # Filter products by name if search term is provided
    if search:
        products_list = products_list.filter(Q(name__icontains=search))
    
    # Filter products by category ID
    if category:
        products_list = products_list.filter(
            product_type__sub_category__category__id=category
        )
        
    # Filter products by sub-category ID
    if sub_category:
        products_list = products_list.filter(
            product_type__sub_category__id=sub_category
        )
        
    # Filter products by brand ID
    if brand:
        products_list = products_list.filter(brand__id=brand)
    
     # Filter products by minimum price
    if price_min:
        products_list = products_list.filter(price__gte=price_min)
     
    # Setup pagination (8 products per page)
    paginator = Paginator(products_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Context to pass sub-categories and brands for the sidebar/filters
    context = {
        "products": page_obj,
        "subCategories": SubCategory.objects.all(),
        "brands": Brand.objects.all()
    }
    return render(request, 'products/products.html', context)

# View to display single product details, including versions (size/color)
def single_product(request, slug):
    products = get_object_or_404(Product, slug=slug) # Fetch product by slug
    sizes = SizeVariant.objects.filter(product=products) # Fetch available sizes
    colors = ColorVariant.objects.filter(product=products) # Fetch available colors
    
    context = {
        "product": products,
        "sizes" : sizes,
        "colors": colors
    }
    return render(request, "products/single-product.html", context)