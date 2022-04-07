from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),           
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
           'last_name': forms.TextInput(attrs={'class':'form-control'}),
           'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
        
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['biography','avatar']
            widgets = {
                'biography': forms.Textarea(attrs={'class':'form-control'}),
                'avatar': forms.FileInput(attrs={'class':'form-control'}),
            }
            labels = {
            'biography': 'Biografía',
            'avatar': 'Avatar',
            }