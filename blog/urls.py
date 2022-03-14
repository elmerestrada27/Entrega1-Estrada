from sre_constants import IN
from django.contrib import admin
from homepage.views import IndexView,AboutView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/', include(('posts.urls'), namespace='post'))    # namespace funciona si se define el nobmre de app, en el archivo urls.py de la App
]