from django.shortcuts import get_object_or_404
from django.views import generic
from posts.models import Post
from .forms import ProfileEditForm, UserEditForm, RegisterForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'Users/user_register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        profile_create=Profile(user=self.object, biography="Mi biografía..")
        profile_create.save()
        return response
class UserEditView(LoginRequiredMixin, generic.UpdateView):
    form_class = UserEditForm
    template_name = 'Users/edit_user.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'Users/profile_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        page_user = get_object_or_404(Profile, pk=self.kwargs['pk'])
        mis_posts = Post.objects.filter(author=page_user.user)
        context.update({'page_user':page_user, 'mis_posts':mis_posts})
        return context

class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'Users/profile_edit.html'
    success_url = reverse_lazy('index')