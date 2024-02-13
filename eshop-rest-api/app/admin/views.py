





from django.template import loader
from django.http import HttpResponse


from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
# from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from ..models.Product import Product
from ..models.Money import Money

from ..serializers import ProductSerializer, MoneySerializer





# ADMIN VIEWS
class ProductREDView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductBAView(ListAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MoneyREDView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer

class MoneyBAView(ListAPIView, CreateAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
    

# ADMIN PAGE VIEWS
def productPage(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render({}, request))

def orderPage(request):
    template = loader.get_template('orders.html')
    return HttpResponse(template.render({}, request))


