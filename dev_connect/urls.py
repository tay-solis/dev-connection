from django.urls import path
from . import views

urlpatterns = [
    path('<username>/', views.student_profile, name='student_profile'),
    path('<username>/projects/<title>', views.project_details, name='project_details'),
    path('', views.all_profiles, name='all_profiles'),
    path('profile/add', views.add_profile, name='add_profile'),

]
