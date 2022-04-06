from django.urls import include, path
from django.contrib.auth import views as auth_views     # Vistas que proporciona Django
from .views import UserRegisterView, UserEditView, ProfileDetailView

app_name = 'user'

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', UserEditView.as_view(), name='perfil'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='detail_profile'),
]