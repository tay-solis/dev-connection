from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class StudentProfile(models.Model):
    tag_line= models.CharField(max_length=50, blank=True)
    location= models.CharField(max_length=50, blank=True)
    linkedin_link = models.CharField(max_length=50, blank=True)
    github_link = models.CharField(max_length=50, blank=True)
    website_link = models.CharField(max_length=50, blank=True)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    skills= models.TextField(blank=True)
    favorite_snack= models.CharField(max_length=50, blank=True)
    dream_job= models.TextField(blank=True)
    favorite_tech= models.CharField(max_length=50, blank=True)
    hidden_talent = models.CharField(max_length=50, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'profile')


class Project(models.Model):
    title= models.CharField(max_length=50)
    hosted_link = models.CharField(max_length=50, blank=True)
    github_link = models.CharField(max_length=50, blank=True)
    screenshot= models.TextField(blank=True)
    description= models.TextField(blank=True)
    tech = models.TextField(blank=True)
    teammates = models.TextField(blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'projects')
