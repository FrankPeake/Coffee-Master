from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import Permission, User
from django.contrib.auth import authenticate, login as dj_login
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType
from .forms import SignUpForm,LoginForm


# Create your views here.
def index(request):
    return render(request, 'thirdplace/index.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            dj_login(request,user)
            return redirect('/thirdplace/')

        else:
            form = LoginForm()
            return render(request,'thirdplace/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request,'thirdplace/login.html', {'form':form})

def signup(request):
    if request.method == 'POST':    
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.city = form.cleaned_data.get('city')
            user.profile.state_province = form.cleaned_data.get('state_province')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            dj_login(request, user)
            return redirect('/thirdplace/')
    else:
        form = SignUpForm()
    return render(request, 'thirdplace/signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/thirdplace/')
    

def browser(request):
    return render(request, 'thirdplace/browser.html')

def bevbuilder(request):
    return render(request, 'thirdplace/bevbuilder.html')