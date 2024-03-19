from rest_framework.authentication import BasicAuthentication
from django.conf import settings
import jwt
from rest_framework import exceptions
from ..models.Client import Client
from ..models.Order import Order





class CustomJWTAuthentication(BasicAuthentication):
    
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        access_token = authorization_header.split(' ')[1]

        try:
            payload = jwt.decode(
                access_token,
                settings.SECRET_KEY,
                algorithms=['HS256']
            )
            client = Client.objects.get(pk=payload['user_id'])
            order = Order.objects.get(pk=payload['order_id'])

            if client is None or order is None:
                raise exceptions.AuthenticationFailed('wrong credentials')


        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('acces token expired')
        
        return (client, None)