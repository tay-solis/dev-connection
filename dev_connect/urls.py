from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.student_profile, name='student_profile'),
    path('', views.all_profiles, name='all_profiles')
]
