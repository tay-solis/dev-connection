from django.shortcuts import render, get_object_or_404
from .models import StudentProfile, Project
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import StudentProfileForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy


students = User.objects.all()

# Create your views here.
def student_profile(request, username):
    student = get_object_or_404(User, username=username)
    profile = get_object_or_404(StudentProfile, user_id=student.id)
    projects = Project.objects.filter(user_id=student.id)
    return render(request, 'dev_connect/profile.html', {'student': student, 'profile': profile, 'projects': projects, 'students': students})

def project_details(request, username, title):
    student = get_object_or_404(User, username=username)
    project = get_object_or_404(Project, title=title)
    return render(request, 'dev_connect/project_details.html', {'student': student, 'project': project, 'students': students})

def all_profiles(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'dev_connect/allprofiles.html', {'profiles': profiles, 'students': students})

<<<<<<< HEAD
=======
@login_required
def add_profile(request):
    if request.method == 'POST':
        username = request.user.username
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user_id = request.user
            new_profile.save()
            return HttpResponseRedirect('/students/' + request.user.username + '/')
    else:
        form = StudentProfileForm()
        return render(request, 'dev_connect/addprofile.html', {'form': form})
>>>>>>> 905daa45d1d13cf3e08843063b3a57ddde8767ce
