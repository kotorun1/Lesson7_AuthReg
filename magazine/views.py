from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Product, Manufacturer, Country, Cart, Order
from .serializers import ProductSerializer, ManufacturerSerializer, CountrySerializer, CartSerializer, OrderSerializer

# CRUD-операции для модели "Manufacturer"

@api_view(['GET'])
@permission_classes([AllowAny])
def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    serializer = ManufacturerSerializer(manufacturers, many=True)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def manufacturer_create(request):
    serializer = ManufacturerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Manufacturer not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = ManufacturerSerializer(manufacturer)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def manufacturer_update(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Manufacturer not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = ManufacturerSerializer(manufacturer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def manufacturer_delete(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Manufacturer not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    manufacturer.delete()
    return JsonResponse({'data':{
                    'message' : 'Manufacturer deleted successfully.'
                    }
                }, status=status.HTTP_204_NO_CONTENT)

# CRUD-операции для модели "Country"

@api_view(['GET'])
@permission_classes([AllowAny])
def country_list(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def country_create(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def country_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Country not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = CountrySerializer(country)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def country_update(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Country not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = CountrySerializer(country, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def country_delete(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Country not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    country.delete()
    return JsonResponse({'data':{
                    'message' : 'Country deleted successfully.'
                    }
                }, status=status.HTTP_204_NO_CONTENT)

# CRUD-операции для модели "Product"

@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Product not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Product not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Product not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return JsonResponse({'data':{
                    'message' : 'Product deleted successfully.'
                    }
                }, status=status.HTTP_204_NO_CONTENT)

# CRUD-операции для модели "Cart"

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_list(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_create(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Cart not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = CartSerializer(cart)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def cart_update(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Cart not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = CartSerializer(cart, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cart_delete(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Cart not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    cart.delete()
    return JsonResponse({'data':{
                    'message' : 'Cart deleted successfully.'
                    }
                }, status=status.HTTP_204_NO_CONTENT)

# CRUD-операции для модели "Order"

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Order not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order)
    return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def order_update(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Order not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def order_delete(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return JsonResponse({'error':{
                    'code' : 404,
                    'message' : 'Order not found.'
                    }
                }, status=status.HTTP_404_NOT_FOUND)
    order.delete()
    return JsonResponse({'data':{
                    'message' : 'Order deleted successfully.'
                    }
                }, status=status.HTTP_204_NO_CONTENT)




