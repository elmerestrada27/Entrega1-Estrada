from django.urls import path
from .views import CategoryCreateView, CategoryListView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name="list"),
    path('create/', PostCreateView.as_view(), name="create"),
    path('<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('<int:pk>/update', PostUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name="delete"),
    
    path('categoria/', CategoryCreateView.as_view(), name='categoria'),  
    path('listado_categoria/', CategoryListView.as_view(), name='list_categoria'),  
]
