from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.
class StudentProfile(models.Model):
    tag_line= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    linkedin_link = models.CharField(max_length=50)
    github_link = models.CharField(max_length=50)
    website_link = models.CharField(max_length=50)
    image= models.TextField()
    skills= models.TextField()
    favorite_snack= models.CharField(max_length=50)
    dream_job= models.TextField()
    favorite_tech= models.CharField(max_length=50)
    hidden_talent = models.CharField(max_length=50)
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
