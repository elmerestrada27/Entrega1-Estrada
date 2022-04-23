from django.urls import path
from django.contrib.auth import views as auth_views
from .views import LoginFormView, PasswordEditView, ProfileEditView, UserRegisterView, UserEditView, ProfileDetailView

app_name = 'user'

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings/', UserEditView.as_view(), name='edit_user'),
    path('settings/password', PasswordEditView.as_view(), name='change_password'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='detail_profile'),
    path('profile/<int:pk>/update', ProfileEditView.as_view(), name='edit_profile'),
]