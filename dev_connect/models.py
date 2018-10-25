from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.
class StudentProfile(models.Model):
    tag_line= models.CharField(max_length=50)
    location= models.CharField(max_length=50)
    image= models.TextField()
    skills= ArrayField(models.CharField(max_length=25))
    favorite_snack= models.CharField(max_length=50)
    dream_job= models.TextField()
    favorite_tech= models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'profile')


class Project(models.Model):
    title= models.CharField(max_length=50)
    screenshot= models.TextField()
    description= models.TextField()
    tech= ArrayField(models.CharField(max_length=25))
    teammates= ArrayField(models.CharField(max_length=25))
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'projects')
