from django.shortcuts import render
from .models import StudentProfile, Project

# Create your views here.
def student_profile(request,pk):
    student = get_object_or_404(User, id=pk)
    profile = get_object_or_404(StudentProfile, id=pk, user_id=user.id)
    return render(request, 'dev_connect/profile.html', {'user': user, 'profile': profile})
