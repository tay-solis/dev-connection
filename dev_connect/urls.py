from django.urls import path
from . import views

urlpatterns = [
    path('student/<id:pk>/', views.student_profile, name='student_profile'),
]
