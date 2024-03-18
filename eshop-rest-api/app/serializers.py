





from rest_framework import serializers
from .models.Product import Product
from .models.Money import Money

from .models.Order import Order
from .models.Image import Image



class ProductSerializer(serializers.ModelSerializer):
    
    #configuation
    class Meta:
        model = Product
        fields = ['id', 'name', 'description',
                  'price_standard', 'price_discount']
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','file','product']


class OrderSerializer(serializers.ModelSerializer):
    
    #configuation
    class Meta:
        model = Order
        fields = ['id', 'created', 'client_id']



class MoneySerializer(serializers.ModelSerializer):
    
    #configuation
    class Meta:
        model = Money
        fields = ['id', 'amount', 'currency']