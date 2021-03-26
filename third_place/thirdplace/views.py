from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    return render(request, 'thirdplace/index.html')

def login(request):
    return render(request, 'thirdplace/login.html')

def signup(request):
    return render(request, 'thirdplace/signup.html')

def browser(request):
    return render(request, 'thirdplace/browser.html')

def bevbuilder(request):
    return render(request, 'thirdplace/bevbuilder.html')