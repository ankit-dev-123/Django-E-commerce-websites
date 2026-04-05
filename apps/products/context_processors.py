from .models import Category

# Context processor to provide all active categories to every template
def categories(request):
    # Returns only categories where is_active is True, sorted alphabetically by name
    return {
        'categories': Category.objects.filter(is_active=True).order_by('name')
    }
