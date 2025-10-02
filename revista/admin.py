from django.contrib import admin
from .models import Estudiante, Autor, Revisor, Articulo, Comentario

admin.site.register(Estudiante)
admin.site.register(Autor)
admin.site.register(Revisor)
admin.site.register(Articulo)
admin.site.register(Comentario)
