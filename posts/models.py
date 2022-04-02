from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    #content_image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Eliminacion en cascada: Si se elimina un usuario se eliminan los Post relacionados a este.
    publish_date = models.DateTimeField(auto_now_add=True)  # Cuando se publica se agrega automaticamente la fecha actual
    last_update = models.DateTimeField(auto_now=True)
    # Vincular tablas

    def __str__(self):
        return self.title
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    activo = models.BooleanField()
    
    def __str__(self):
        return f'{self.nombre}'