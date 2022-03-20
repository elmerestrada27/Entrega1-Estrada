from django.contrib import admin

from .models import Categoria, Post, Usuario

admin.site.register(Post)
admin.site.register(Usuario)
admin.site.register(Categoria)