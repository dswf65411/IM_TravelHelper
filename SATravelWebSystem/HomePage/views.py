from django.shortcuts import render

# Create your views here.
def home(request) :
    region1 = {'region': '台北', 'school': '臺大', 'name': '臺  大', 'image': 'static/images/taiwan_university.png'}
    region2 = {'region': '新竹', 'school': '清大', 'name': '清  大', 'image': 'static/images/chin-hua.png'}
    region3 = {'region': '新竹', 'school': '交大', 'name': '交  大', 'image': 'static/images/mrt.png'}
    post = [region1, region2, region3]
    images = ['static/images/ranbow.png', 'static/images/paper.png',
            'static/images/sasasa.png', 'static/images/beauty.png',
            'static/images/water.png', 'static/images/sunset.png']
    return  render(request, 'home.html', {
        'top_regions': post,
        'images': images
    })

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, 'login.html')

def finish(request):
    return render(request, 'finish.html')

def login_finish(request):
    return render(request, 'finish2.html')
