from django.shortcuts import render

# Create your views here.
def addTrip(request):
    if request.method == "POST" :
        introWriting = request.POST.get('introWriting', '')
        password = request.POST.get('password', '')
    return render(request, 'addTrip.html')
