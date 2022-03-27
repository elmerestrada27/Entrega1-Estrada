#from django.shortcuts import render
from django.views.generic import TemplateView

from posts.models import Post

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super ().get_context_data(**kwargs)
        gq = Post.objects.all().order_by('-id')[:6] 
        context.update({                            # Se añade un nuevo dato de contexto para actualizar vista Form
            'ultimos_post': gq
        })
        return context

class AboutView(TemplateView):
    template_name = 'about.html'