from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404



def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    ######DO PASSWORDS MATCH?#########
    if password == password2:
    #####DOES USERNAME EXIST ALREADY?#######
      if User.objects.filter(username=username).exists():
        return render(request, 'accounts/register.html', {'error': 'Username already registered.  Please choose a different username.'})
      else:
        #####CHECK FOR EMAIL######
        if User.objects.filter(email=email).exists():
          return render(request, 'accounts/register.html', {'error': 'That email has already been registered.'})
    #########REGISTER USER#######
        else:
          user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
          user.save()
          new_user = auth.authenticate(username=username,password=password)
          auth.login(request, user)
        return HttpResponseRedirect("../../students/profile/add")
    else:
      return render(request, 'accounts/register.html', {'error': 'Passwords do not match.'})
  else:
    return render(request, 'accounts/register.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'accounts/login.html', {'error': 'Invalid credentials.'})
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  auth.logout(request)
  return redirect('home')
