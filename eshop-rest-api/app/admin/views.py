





from django.template import loader
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status


from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
# from rest_framework.mixins import ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from ..models.Product import Product
from ..models.Money import Money
from ..models.Image import Image


from ..serializers import ProductSerializer, MoneySerializer, ImageSerializer





# ADMIN VIEWS
class ProductREDView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductBAView(ListAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageAView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



#B[R][E]A[D]
class MoneyREDView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer

#[B]RE[A]D
class MoneyBAView(ListAPIView, CreateAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
    

class MoneyBCustomView(APIView):
    def get(self, reguest, pks):
        ids = pks.split(',')
        money = Money.objects.filter(id__in=ids)
        serialized_data = MoneySerializer(money, many=True)
        return Response(serialized_data.data)

class ImagesBCustomView(APIView):
    def get(self, reguest, pks):
        ids = pks.split(',')
        images = Image.objects.filter(product__in=ids)
        serialized_data = ImageSerializer(images, many=True)
        return Response(serialized_data.data)



# ADMIN PAGE VIEWS
def productPage(request):
    template = loader.get_template('products.html')
    return HttpResponse(template.render({}, request))

def orderPage(request):
    template = loader.get_template('orders.html')
    return HttpResponse(template.render({}, request))


