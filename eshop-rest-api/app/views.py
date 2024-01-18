






from rest_framework import generics
from .models.Product import Product
from .serializers import ProductSerializer

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAdminView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # TODO: acces policy
