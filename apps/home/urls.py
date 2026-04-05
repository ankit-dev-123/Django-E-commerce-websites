from django.urls import path
from .views import home

# URL patterns for the home app
urlpatterns = [
    # URL for the main landing page, mapped to the home view
    path('', home, name='home'),
]