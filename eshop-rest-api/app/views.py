






from rest_framework import generics, status
from .models.Product import Product
from .models.Order import Order
from .models.OrderItem import OrderItem
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.response import Response

#PUBLIC VIEWS
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

         # CUSTOM: OrderItem creation here
        product_id = kwargs.get('uuid')      
        order_item = OrderItem(
             product = Product.objects.get(pk = product_id),
             order = Order.objects.get(pk=serializer.data.get('id'))
         )
        order_item.save()
        # CUSTOM: OrderItem creation here

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


 










# ADMIN VIEWS
class ProductAdminView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # TODO: acces policy
