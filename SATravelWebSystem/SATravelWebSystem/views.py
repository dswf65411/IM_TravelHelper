from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from mongoDB.connection import connect

def register(request):
    if request.method == 'POST':
        account = request.POST.get('id_account', '');
        name = request.POST.get('id_username', '');
        sex = request.POST.get('id_sex', '');
        phone = request.POST.get('id_phone', '');
        password1 = request.POST.get('id_password1', '');
        password2 = request.POST.get('id_password2', '');
        email = request.POST.get('id_email', '');
        isGuide = False;
        if password1 == password2:
            post = {
                "account": account,
                "name" : name,
                "sex" : sex,
                "phone" : phone,
                "password" : password1,
                "email" : email,
                "isGuide" : isGuide
            }
            registerConnect(post)
            return redirect('finish')
        else:
            return render_to_response('register.html', RequestContext(request, locals()))
    else:
        return render_to_response('register.html', RequestContext(request, locals()))

def login(request):
    if request.session.get('account', '') != '':
        account = request.session.get('account', '')
        username = sessionConnect(account)
    #     return render_to_response('home.html', RequestContext(request, locals()))
    if request.method == 'POST':
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        username = loginConnect(account, password)
        if username != '':
            request.session['account'] = account
            return redirect('home')
    username = ''
    return render_to_response('login.html', RequestContext(request, locals()))

def finish(request):
    return render(request, 'finish.html')

def logout(request):
    if request.session.get('account', '') != '':
        del request.session['account']
    username = ''
    return redirect('home')

def registerConnect(post):
    DB = connect()
    collect = DB['使用者']
    collect.insert_one(post)
    return

def sessionConnect(account):
    DB = connect()
    collect = DB['使用者']
    username = collect.find({'account': account},{'name':1,'_id':0})[0]['name']
    return username

def loginConnect(account, password):
    DB = connect()
    collect = DB['使用者']
    user = collect.find({'account': account},{'password':1,'name':1,'_id':0})[0]
    if user['password'] == password:
        return user['name']
    else :
        return ''
