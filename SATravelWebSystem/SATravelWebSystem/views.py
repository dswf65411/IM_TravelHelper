from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .user import UserCreateForm
from django.template import RequestContext

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('finish')
    else:
        form = UserCreateForm()
    return render_to_response('register.html', RequestContext(request, locals()))

def login(request):
    if request.user.is_authenticated():
        return redirect('home')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('home')
    return render_to_response('login.html', RequestContext(request, locals()))

def finish(request):
    return render(request, 'finish.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
