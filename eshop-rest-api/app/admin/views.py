






from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
# from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from ..models.Product import Product
from ..serializers import ProductSerializer





# ADMIN VIEWS
class ProductREADView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductBView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    