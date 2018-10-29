from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.
class StudentProfile(models.Model):
    tag_line= models.CharField(max_length=50, blank=True)
    location= models.CharField(max_length=50, blank=True)
    linkedin_link = models.CharField(max_length=50, blank=True)
    github_link = models.CharField(max_length=50, blank=True)
    website_link = models.CharField(max_length=50, blank=True)
    image= models.TextField(blank=True)
    skills= models.TextField(blank=True)
    favorite_snack= models.CharField(max_length=50, blank=True)
    dream_job= models.TextField()
    favorite_tech= models.CharField(max_length=50, blank=True)
    hidden_talent = models.CharField(max_length=50, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'profile')


class Project(models.Model):
    title= models.CharField(max_length=50)
    hosted_link = models.CharField(max_length=50)
    github_link = models.CharField(max_length=50)
    screenshot= models.TextField()
    description= models.TextField()
    tech = models.TextField()
    teammates = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'projects')
