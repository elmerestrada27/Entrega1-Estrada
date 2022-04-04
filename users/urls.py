from django.urls import include, path
from users.views import UserRegisterView,UserEditView
from django.contrib.auth import views as auth_views     # Vistas que proporciona Django

app_name = 'user'

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', UserEditView.as_view(), name='perfil'),
]