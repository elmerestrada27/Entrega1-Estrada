from cProfile import label
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.shortcuts import render


class PostListView(ListView):
    model = Post
    template_name = 'Posts/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'Posts/post_detail.html'
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Posts/post_form.html'
    #succes_url = "/Posts/post/post_list"
    success_url = reverse_lazy('post:list')         # Para redirigir al usuario luego de crear un post --> Hace referencia al name que se asigna en posts/urls.py --> NO al nombre del template
    #fields = ('title', 'content')                  # No permite configurar form_class y fields (solo uno)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post:list')
    

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'Posts/post_delete.html'    
    success_url = reverse_lazy('post:list')
