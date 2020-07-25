from django.urls import path, include
from apps.tienda.views import index

urlpatterns = [
    path('',index),
]
