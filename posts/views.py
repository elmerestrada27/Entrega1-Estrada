from .models import Category, Post
from .forms import  CategoryForm, PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
class PostListView(ListView):
    model = Post
    template_name = 'Posts/post_list.html'
    ordering = ['-id']

    def get_queryset(self):
        gq = Post.objects.all().order_by('-id')         # Los utlimos post se visualizaran primero
        post_a_buscar = self.request.GET.get('buscar')  # Necesito hacer referencia al nombre del input: 'buscar'!!
        if post_a_buscar:
            gq = gq.filter(title__icontains=post_a_buscar)
        return gq           

class PostDetailView(DetailView):
    model = Post
    template_name = 'Posts/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    # Por defecto CreateView y UpdateView toman como template: 'nombreModelo_form'
    model = Post
    form_class = PostForm
    template_name = 'Posts/postCreate_form.html'
    success_url = reverse_lazy('post:list')         # Para redirigir al usuario luego de crear un post --> Hace referencia al name que se asigna en posts/urls.py --> NO al nombre del template
    #fields = ('title', 'content')                  # No permite configurar form_class y fields (solo uno)

    def form_valid(self, form):                     # Esto me permite asignar un Autor (usuario logueadi) a un post, cuando este es creado
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):         # Separe los templates para crear y actualizar, no es necesario distinguir de donde viene la peticion
    #     context = super ().get_context_data(**kwargs)
    #     context.update({                            # Se añade un nuevo dato de contexto para actualizar vista Form
    #         'tipo_vista': 'create'
    #     })
    #     return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm      
    template_name = 'Posts/postUpdate_form.html'                     
    success_url = reverse_lazy('post:list')  

    # def get_context_data(self, **kwargs):           # Separe los templates para crear y actualizar, no es necesario distinguir de donde viene la peticion
    #     context = super ().get_context_data(**kwargs)
    #     context.update({                              # Se añade un nuevo dato de contexto para actualizar vista Form
    #         'tipo_vista': 'update'
    #     })
    #     return context

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'Posts/post_delete.html'        # DeleteView necesita una ventana de confirmacion para realizar la eliminacion
    success_url = reverse_lazy('post:list')

# ------------------------------------------------------
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'Posts/categoria_create.html'
    success_url = reverse_lazy('post:list_categoria') 

class CategoryListView(ListView):
    model = Category
    template_name = 'Posts/categoria_list.html'