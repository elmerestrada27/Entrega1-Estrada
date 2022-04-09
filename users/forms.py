from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
        
class ChangePasswordForm(PasswordChangeForm):
    # old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    # new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    # new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        widgets = {
                'old_password': forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
                'new_password1': forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
                'new_password2': forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
            }
        # labels = {
        #     'old_password': 'Contraseña actual',
        #     'new_password1': 'Nueva contraseña',
        #     'new_password2': 'Repetir contraseña',
        #     }
    
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['biography','website_url','avatar']
            widgets = {
                'biography': forms.Textarea(attrs={'class':'form-control'}),
                'website_url': forms.TextInput(attrs={'class':'form-control'}),
                'avatar': forms.FileInput(attrs={'class':'form-control'}),
            }
            labels = {
            'biography': 'Biografía',
            'website_url': 'Página web',
            'avatar': 'Avatar',
            }