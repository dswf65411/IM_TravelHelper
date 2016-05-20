from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request, 'home.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, 'login.html')

def finish(request):
    return render(request, 'finish.html')

def login_finish(request):
    return render(request, 'finish2.html')
