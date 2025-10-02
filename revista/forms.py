from django import forms
from .models import Estudiante, Autor, Revisor, Articulo, Comentario

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class RevisorForm(forms.ModelForm):
    class Meta:
        model = Revisor
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
