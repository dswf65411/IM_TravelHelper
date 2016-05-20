from django.shortcuts import render

# Create your views here.

def trip(request):
    return render(request, 'trip.html')
