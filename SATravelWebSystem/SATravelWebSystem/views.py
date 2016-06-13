from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from mongoDB.connection import connect
import functools
import pymongo
import logging
import time

MAX_AUTO_RECONNECT_ATTEMPTS = 5

def graceful_auto_reconnect(mongo_op_func):
  """Gracefully handle a reconnection event."""
  @functools.wraps(mongo_op_func)
  def wrapper(*args, **kwargs):
    for attempt in xrange(MAX_AUTO_RECONNECT_ATTEMPTS):
      try:
        return mongo_op_func(*args, **kwargs)
      except pymongo.errors.AutoReconnect as e:
        wait_t = 0.5 * pow(2, attempt) # exponential back off
        logging.warning("PyMongo auto-reconnecting... %s. Waiting %.1f seconds.", str(e), wait_t)
        time.sleep(wait_t)

  return wrapper

def register(request):
    if request.method == 'POST':
        account = request.POST.get('account', '');
        name = request.POST.get('username', '');
        sex = request.POST.get('sex', '');
        phone = request.POST.get('phone', '');
        password1 = request.POST.get('password1', '');
        password2 = request.POST.get('password2', '');
        email = request.POST.get('email', '');
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
            graceful_auto_reconnect(registerConnect(post))
            return redirect('finish')
        else:
            return render_to_response('register.html', RequestContext(request, locals()))
    else:
        return render_to_response('register.html', RequestContext(request, locals()))

def login(request):
    if request.session.get('account', '') != '':
        account = request.session.get('account', '')
        username = graceful_auto_reconnect(sessionConnect(account))
    #     return render_to_response('home.html', RequestContext(request, locals()))
    if request.method == 'POST':
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        username = graceful_auto_reconnect(loginConnect(account, password))
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
