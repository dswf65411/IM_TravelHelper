from django.shortcuts import render

# Create your views here.

def list(request):
    name = '臺大'
    region = '台北'
    if 'region' in request.GET and request.GET['region'] != '':
        region = request.GET['region']
    if 'school' in request.GET and request.GET['school'] != '':
        name = request.GET['school']
    return  render(request, 'list.html', {
        'name': name,
        'region': region
    })
