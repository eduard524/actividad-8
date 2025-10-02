from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carnet = models.CharField(max_length=20, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.carnet})"

class Autor(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Autor: {self.estudiante.nombre}"

class Revisor(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Revisor: {self.estudiante.nombre}"

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    revisor = models.ForeignKey(Revisor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.nombre} comentó en {self.articulo.titulo}"
