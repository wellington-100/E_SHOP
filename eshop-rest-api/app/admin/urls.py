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
from django.urls import path
from .views import *



urlpatterns = [
    # administrative API routes
    path('products/image', ProductImageAView.as_view()),

    path('products/<uuid:pk>', ProductREDView.as_view()),
    path('products/', ProductBAView.as_view()),

    path('money/<uuid:pk>', MoneyREDView.as_view()),

    # ideally -reagular expression of a list of uuids separated by coma
    path('money/multi/<str:pks>', MoneyBCustomView.as_view()),
    path('images/multi/<str:pks>', ImagesBCustomView.as_view()),

    path('money/', MoneyBAView.as_view()),

    # administrative  TEMPLATES pages / routes
    path('products-page', productPage),
    path('orders-page', orderPage)
]
