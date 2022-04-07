from django.urls import include, path
from django.contrib.auth import views as auth_views     # Vistas que proporciona Django
from .views import ProfileEditView, UserRegisterView, UserEditView, ProfileDetailView
from .forms import ChangePasswordForm
from django.urls import reverse_lazy

app_name = 'user'

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('settings/', UserEditView.as_view(), name='edit_user'),
    # path('settings/password', 
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='Users/change_password.html',
    #         form_class='ChangePasswordForm',
    #         success_url=reverse_lazy('index')), 
    #     name='change_password'),
    # path('settings/password/done/',
    #         auth_views.PasswordChangeView.as_view(
    #         template_name='Users/change_password_done.html'
    #  ), 
    #  name='password_change_done')
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='detail_profile'),
    path('profile/<int:pk>/update', ProfileEditView.as_view(), name='edit_profile'),
]