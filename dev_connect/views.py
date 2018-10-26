from django.shortcuts import render, get_object_or_404
from .models import StudentProfile, Project
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def student_profile(request, username):
    student = get_object_or_404(User, username=username)
    profile = get_object_or_404(StudentProfile, user_id=student.id)
    projects = Project.objects.filter(user_id=student.id)
    return render(request, 'dev_connect/profile.html', {'student': student, 'profile': profile, 'projects': projects})

def project_details(request, username, title):
    student = get_object_or_404(User, username=username)
    project = get_object_or_404(Project, title=title)
    return render(request, 'dev_connect/project_details.html', {'student': student, 'project': project})

def all_profiles(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'dev_connect/allprofiles.html', {'profiles': profiles})
