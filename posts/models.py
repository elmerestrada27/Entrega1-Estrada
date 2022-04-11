from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    # content = models.TextField(max_length=255)
    content = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    content_image = models.ImageField(null=True, blank=True, upload_to='images/post/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Eliminacion en cascada: Si se elimina un usuario se eliminan los Post relacionados a este.
    publish_date = models.DateTimeField(auto_now_add=True)  # Cuando se publica se agrega automaticamente la fecha actual
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + '|' + str(self.author)
