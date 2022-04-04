from django.views import generic
from .forms import ProfileEditForm, RegisterForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'Users/user_register.html'
    success_url = reverse_lazy('user:login')

class UserEditView(generic.UpdateView):
    form_class = ProfileEditForm
    template_name = 'Users/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user