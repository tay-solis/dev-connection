from django.shortcuts import render
from .models import StudentProfile, Project
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def student_profile(request, username):
    student = User.objects.filter(username=username)

    return render(request, 'dev_connect/profile.html', {'student': student})

def all_profiles(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'dev_connect/allprofiles.html', {'profiles': profiles})
