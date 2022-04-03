from django import forms
from .models import Category, Post
class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ('title', 'category', 'content',)
        widgets = {                                                        # Me permite utilizar bootstrap para el form
           'title': forms.TextInput(attrs={'class':'form-control'}),
           'category': forms.Select(attrs={'class':'form-control'}),
           'content': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
           'title': 'Titulo',
           'category': 'Categoria',
           'content': 'Contenido',
        }
class CategoryForm(forms.ModelForm):
     class Meta:
        model = Category
        fields = '__all__'
        widgets = {                                                        # Me permite utilizar bootstrap para el form
           'name': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
           'name': 'Nombre',
        }