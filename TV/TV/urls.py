"""TV URL Configuration

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
from django.urls import path, include

# Cargando urls de apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('apps.tienda.urls')),
    path('registro/', include('apps.registro.urls')),
    path('productos/', include('apps.productos.urls')),
    path('cliente/', include('apps.cliente.urls')),
    path('carrito/', include('apps.carrito.urls')),
    path('administrador/', include('apps.administrador.urls')),
    path('compra/', include('apps.compra.urls')),
]
