from django.views import generic
from .forms import RegisterForm
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'Users/register.html'
    success_url = reverse_lazy('user:login')
