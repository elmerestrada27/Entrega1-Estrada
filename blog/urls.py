from django.contrib import admin
from homepage.views import IndexView,AboutView
from posts.views import CategoryCreateView, CategoryListView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # path('categoria/', CategoryCreateView.as_view(), name='categoria'),  
    # path('listado_categoria/', CategoryListView.as_view(), name='list_categoria'),  

    path('about/', AboutView.as_view(), name='about'),
    path('pages/', include(('posts.urls'), namespace='post')),    # namespace funciona si se define el nobmre de app, en el archivo urls.py de la App

    path('accounts/', include(('users.urls'), namespace='user'))    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # Para trabajar con imagenes