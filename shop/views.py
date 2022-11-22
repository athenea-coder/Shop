from django.shortcuts import render
from django.http import HttpResponse

def shopView(request):
    return render(request, 'shop/index.html')
def shopContactUs(request):
    return render(request, 'shop/static/nosotros/nosotros.html')
def shopProductos(request):
    return render(request, 'shop/static/productos/productos.html')    
def shopLogin(request):
    return render(request,'shop/static/login/login.html')
  