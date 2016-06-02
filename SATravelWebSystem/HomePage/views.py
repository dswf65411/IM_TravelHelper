from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth

# Create your views here.
def home(request) :
    # if request.POST :
    #     account = request.POST['account']
    #     password = request
    region1 = {'region': '台北', 'school': '臺大', 'name': '臺  大', 'image': 'static/images/taiwan_university.png'}
    region2 = {'region': '新竹', 'school': '清大', 'name': '清  大', 'image': 'static/images/chin-hua.png'}
    region3 = {'region': '新竹', 'school': '交大', 'name': '交  大', 'image': 'static/images/mrt.png'}
    top_regions = [region1, region2, region3]
    images = ['static/images/ranbow.png', 'static/images/paper.png',
            'static/images/sasasa.png', 'static/images/beauty.png',
            'static/images/water.png', 'static/images/sunset.png']
    return  render_to_response('home.html', RequestContext(request, locals()))
