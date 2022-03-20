from django import forms
from .models import Categoria, Post, Usuario

class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('title', 'content',)
        widgets = {                                                        # Me permite utilizar bootstrap para el form
           'title': forms.TextInput(attrs={'class':'form-control'}),
           'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
           'title': 'Titulo',
           'content': 'Contenido',
        }

# class BusquedaForm(forms.ModelForm):
#    class Meta:
#       fields = ('title',)

class UsuarioForm(forms.ModelForm):
     class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {                                                        # Me permite utilizar bootstrap para el form
           'nombre': forms.TextInput(attrs={'class':'form-control'}),
           'apellido': forms.TextInput(attrs={'class':'form-control'}),
           'email': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
           'nombre': 'Nombre',
           'apellido': 'Apellido',
           'email': 'Email'
        }

class UsuarioBusquedaForm(forms.Form):
      nombre = forms.CharField(max_length=20, required=False)
      widgets = {                                                        # Me permite utilizar bootstrap para el form
           'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }


class CategoriaForm(forms.ModelForm):
     class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {                                                        # Me permite utilizar bootstrap para el form
           'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }
      #   labels = {
      #      'nombre': 'Nombre',
      #      'apellido': 'Apellido',
      #      'email': 'Email'
      #   }