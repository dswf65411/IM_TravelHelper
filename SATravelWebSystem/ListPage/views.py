from django.shortcuts import render
from mongoDB.connection import connect
from SATravelWebSystem.views import sessionConnect, graceful_auto_reconnect

# Create your views here.

def list(request):
    if request.session.get('account', '') != '':
        account = request.session.get('account', '')
        username = graceful_auto_reconnect(sessionConnect(account))
    else:
        username = ''
    name = '台大'
    region = '台北'
    if 'region' in request.GET and request.GET['region'] != '' and 'school' in request.GET and request.GET['school'] != '':
        region = request.GET['region']
        name = request.GET['school']
    regions = ['台北', '新竹', '台中', '台南', '高雄']
    orders = [{
                'tag' : '熱門度：高 到 低',
                'order' : 'hot'
            }, {
                'tag' : '價格：低 到 高',
                'order' : 'price'
            }, {
                'tag' : '價格：高 到 低',
                'order' : '-price'
            }
    ]
    regions.remove(region)
    trips = listConnect(region, name)
    if 'order' in request.GET and request.GET['order'] != '':
        order = request.GET['order']
        if order == 'price':
            nowOrder = orders[1]
            orders.pop(1)
            trips = sorted(trips, key=lambda k: k['price'])
        elif order == '-price':
            nowOrder = orders[2]
            orders.pop(2)
            trips = sorted(trips, key=lambda k: k['price'], reverse = True)
        else:
            nowOrder = orders[0]
            orders.pop(0)
            trips = sorted(trips, key=lambda k: k['star'], reverse = True)
    else:
        nowOrder = orders[0]
        orders.pop(0)
        trips = sorted(trips, key=lambda k: k['star'], reverse = True)
    return  render(request, 'list.html', locals())


def listConnect(region, school):
    DB = connect()
    collect = DB[region]
    temp = collect.find({'name': school },{'trip':1,'_id':0})[0]
    relist = temp['trip']
    for item in relist:
        countingStar = 0
        for count in item['star']:
            countingStar += count['score']
        item['star']=int(countingStar/len(item['star']))
    return relist
