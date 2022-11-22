from django.urls import path
from .views import *
urlpatterns=[
    path('index/', shopView, name='index'),
    path('contactUs/', shopContactUs, name='contactUs'),
    path('productos/', shopProductos, name='productos'),
    path('login/', shopLogin, name='login'),
]