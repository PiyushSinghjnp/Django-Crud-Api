from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# from rest_framework.response import Response
from django.http import HttpResponse
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
