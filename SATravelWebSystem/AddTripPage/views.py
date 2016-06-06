from django.shortcuts import render

# Create your views here.
def addTrip(request):
    return render(request, 'addTrip.html')
