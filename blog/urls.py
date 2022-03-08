from sre_constants import IN
from django.contrib import admin
from homepage.views import IndexView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('post/', include(('posts.urls'), namespace='post'))    # namespace funciona si se define el nobmre de app, en el archivo urls.py de la App
]