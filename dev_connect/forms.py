from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('tag_line', 'location', 'linkedin_link', 'github_link', 'website_link', 'image', 'skills', 'favorite_snack', 'dream_job', 'favorite_tech', 'hidden_talent')
