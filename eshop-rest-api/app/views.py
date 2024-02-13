






from rest_framework import generics, status
from .models.Product import Product
from .models.Money import Money
from .models.Order import Order
from .models.OrderItem import OrderItem
from .serializers import ProductSerializer, OrderSerializer, MoneySerializer
from rest_framework.response import Response
from django.template import loader
from django.http import HttpResponse


# PUBLIC VIEWS
def indexPage(request):
    template = loader.get_template('public/index.html')
    return HttpResponse(template.render({}, request))

