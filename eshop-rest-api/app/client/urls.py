"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views_api import *
from .views_pages import *

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )



urlpatterns = [

    # PUBLIC ROUTES
    path('', indexPage),

    path('products', ProductView.as_view()),
    path('money/<uuid:pk>', MoneyView.as_view()),
    path('orders/<uuid:uuid>', CreateOrderView.as_view()),

    # TOKEN CLIENT ROUTES
    # path('client/token', TokenObtainPairView.as_view()),


    path("client/pay/<uuid:pk>", PaymentView.as_view()),
    # AUTHENTICATED CLIENT ROUTES
    path('client/orders/<uuid:pk>', OrderRView.as_view()),

    
]
