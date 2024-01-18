





from rest_framework import serializers
from .models.Product import Product


class ProductSerializer(serializers.ModelSerializer):
    
    #configuation
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'description']