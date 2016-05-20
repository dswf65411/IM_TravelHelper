from django.shortcuts import render

# Create your views here.

def list(request):
    post = range(0, 4)
    return  render(request, 'list.html', {
        'post': post,
    })
