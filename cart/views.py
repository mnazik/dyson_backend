from django.shortcuts import render
from serializers import CartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem

@api_view(['GET'])
def get_cart(request, user_id):
    cart, created = Cart.objects.get_or_create(user_id=user_id)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    user_id = request.data.get('user_id')
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    cart, created = Cart.objects.get_or_create(user_id=user_id)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_id=product_id
        )
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity

    item.save()

    return Response({'message': 'added'})
