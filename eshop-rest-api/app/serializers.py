





from rest_framework import serializers
from .models.Product import Product
from .models.Order import Order


class ProductSerializer(serializers.ModelSerializer):
    
    #configuation
    class Meta:
        model = Product
        fields = ['id', 'name', 'image','description',
                  'price_standard', 'price_discount']

class OrderSerializer(serializers.ModelSerializer):
    
    #configuation
    class Meta:
        model = Order
        fields = ['id', 'created']