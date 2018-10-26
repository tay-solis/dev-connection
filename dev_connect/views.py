from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DetailView
)
from .models import StudentProfile, Project


def student_profile(request, username):
    student = User.objects.filter(username=username)

    return render(request, 'dev_connect/profile.html', {'student': student})

def all_profiles(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'dev_connect/allprofiles.html', {'profiles': profiles})

class PostListView(ListView):
    model = StudentProfile
    template_name = 'dev_connecct/profile.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'profile'
    oredering = ['-date_posted']
    paginate_by = 5

# class UserPostListView(Listview):
#     model = StudentProfile
#     template_name = 'dev_connect/project_details.html'
#     context_object_name = 'profile'
#     oredering = ['-date_posted']
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Profile.objects.filter(author=user).order_by('-date_posted')

# class PostDetail(DetailView):
#     model = StudentProfile

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = StudentProfile
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False

# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = StudentProfile
#     success_url = '/'

#     def test_func(self):
#         post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




