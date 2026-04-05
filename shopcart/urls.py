from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Main URL configuration for the entire shopcart project
urlpatterns = [
    # URL path for the Django admin administration panel
    path('admin/', admin.site.urls),
    # Default route that includes URLs from the 'home' application
    path('', include('apps.home.urls')),
    # Nested route for all product-related URLs (listing, details)
    path('products/', include('apps.products.urls')),
    # Route for shopping cart functionality (add, remove, view)
    path('cart/', include('apps.cart.urls')),
    # Route for user authentication and account management (login, register)
    path('accounts/', include('apps.accounts.urls'))
]

# Serves uploaded media files (e.g., product images) during development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)