"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, url
from Tienda.views import TiendaView, ProductoView, CompraView


urlpatterns = [
    url(r'^$', TiendaView.as_view(), name='home'),
    url(r'^productos/nuevo', ProductView.as_view(), name='productoView'),
    url(r'^compra', CompraView.as_view(), name='compraView'),
    url(r'^admin/', include(admin.site.urls)),
]
