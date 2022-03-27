from django.shortcuts import render
from .models import Categoria, Post, Usuario
from .forms import  CategoriaForm, PostForm, UsuarioBusquedaForm, UsuarioForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class PostCreateView(CreateView):
    # Por defecto CreateView y UpdateView toman como template: 'nombreModelo_form'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post:list')         # Para redirigir al usuario luego de crear un post --> Hace referencia al name que se asigna en posts/urls.py --> NO al nombre del template
    #fields = ('title', 'content')                  # No permite configurar form_class y fields (solo uno)

    def get_context_data(self, **kwargs):
        context = super ().get_context_data(**kwargs)
        context.update({                            # Se añade un nuevo dato de contexto para actualizar vista Form
            'tipo_vista': 'create'
        })
        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm                           
    success_url = reverse_lazy('post:list')  

    def get_context_data(self, **kwargs):           # Se añade un nuevo dato de contexto para actualizar vista Form
        context = super ().get_context_data(**kwargs)
        context.update({
            'tipo_vista': 'update'
        })
        return context

class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    template_name = 'Posts/post_delete.html'        # DeleteView necesita una ventana de confirmacion para realizar la eliminacion
    success_url = reverse_lazy('post:list')

# ------------------------------------------------------
class UserCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('list_users')         


def lista_usuarios(request):    
    nombre_usuario = request.GET.get('nombre', None)
    encontro = False
    if nombre_usuario:
        users = Usuario.objects.filter(nombre__icontains=nombre_usuario)
        encontro = True
    else:
        users = Usuario.objects.all()
        encontro = False
    form = UsuarioBusquedaForm()
    return render(request, "user_list.html", {'form': form, 'users': users, 'encontro': encontro})

# ------------------------------------------------------
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria_create.html'
    success_url = reverse_lazy('list_categoria') 

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'