from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include(('posts.urls'), namespace='post'))    # namespace funciona si se define el nobmre de app, en el archivo urls.py de la App
]