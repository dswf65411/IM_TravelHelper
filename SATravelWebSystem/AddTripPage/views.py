from django.shortcuts import render
from mongoDB.connection import connect
from django.shortcuts import redirect

# Create your views here.
def addTrip(request):
    if request.method == "POST" :
        title = request.POST.get('title', '')
        price = request.POST.get('price', '')
        introWriting = request.POST.get('introWriting', '')
        travelWriting1 = request.POST.get('travelWriting1', '')
        travelWriting2 = request.POST.get('travelWriting2', '')
        travelWriting3 = request.POST.get('travelWriting3', '')
        siteTitle1 = request.POST.get('siteTitle1', '')
        siteTitle2 = request.POST.get('siteTitle2', '')
        siteTitle3 = request.POST.get('siteTitle3', '')
        post = {
            "title" : title,
            "hour" : 3,
            "price" : int(price),
            "description" : introWriting,
            "categories": ["一日遊"],
            "star" : [
                {
                    "tourist" : "default",
                    "score" : 4
                }
            ],
            "image" : "1.png" ,
            "guide" : request.session['account'],
            "site" : [{
                "name" : siteTitle1,
                "description" : travelWriting1,
                "image" : "1.png"
            },
            {
                "name" : siteTitle2,
                "description" : travelWriting2,
                "image" : "water.png"
            },
            {
                "name" : siteTitle3,
                "description" : travelWriting3,
                "image" : "ranbow.png"
            }
            ],
            "comments":[]
        }
        addTripConnect(post)

        return redirect('home')

    return render(request, 'addTrip.html')

def addTripConnect(post):
    DB = connect()
    collect = DB['台北']
    temp = collect.find({'name': '台大' },{'trip':1,'_id':0})[0]['trip']
    number = len(temp)
    post["tripID"] = number+1
    collect.update({ 'name':'台大'},{'$push':{'trip':post}})
