from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from SATravelWebSystem.views import sessionConnect, graceful_auto_reconnect

# Create your views here.
def home(request) :
    if request.session.get('account', '') != '':
        account = request.session.get('account', '')
        username = graceful_auto_reconnect(sessionConnect(account))
    else:
        username = ''
    region1 = {'region': '台北', 'school': '台大', 'name': '台  大', 'image': 'static/images/taiwan_university.png'}
    region2 = {'region': '新竹', 'school': '清大', 'name': '清  大<br><b>Comming Soon...</b>', 'image': 'static/images/chin-hua.png'}
    region3 = {'region': '新竹', 'school': '交大', 'name': '交  大<br><b>Comming Soon...</b>', 'image': 'static/images/mrt.png'}
    top_regions = [region1, region2, region3]
    images = ['static/images/ranbow.png', 'static/images/paper.png',
            'static/images/sasasa.png', 'static/images/beauty.png',
            'static/images/water.png', 'static/images/sunset.png']
    return  render_to_response('home.html', RequestContext(request, locals()))
