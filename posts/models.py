from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    #content_image = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True) # Cuando se publica se agrega automaticamente la fecha actual
    last_update = models.DateTimeField(auto_now=True)
    # Vincular tablas

    def __str__(self):
        return self.title
