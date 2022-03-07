from django import forms
from .models import Post

class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('title', 'content',)
        labels = {
           'title': 'Titulo',
           'content': 'Contenido',
        }
      #   labels = {'title' : 'Titulo', 'content' : 'Contenido',} # No ANDAA


