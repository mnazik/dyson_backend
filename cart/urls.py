from django.urls import path
from views import get_cart, add_to_cart

urlpatterns = [
    path('cart/<int:user_id>/', get_cart),
    path('add/', add_to_cart),
]