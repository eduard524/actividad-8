from django.shortcuts import render
from .models import Articulo

def index(request):
    articulos = Articulo.objects.all()
    return render(request, "revista/index.html", {"articulos": articulos})
