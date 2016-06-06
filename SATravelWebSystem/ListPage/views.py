from django.shortcuts import render

# Create your views here.

def list(request):
    name = '臺大'
    region = '台北'
    if 'region' in request.GET and request.GET['region'] != '' and 'school' in request.GET and request.GET['school'] != '':
        region = request.GET['region']
        name = request.GET['school']
        regions = ['台北', '新竹', '台中', '台南', '高雄']
        regions.remove(region)
        trip1 = {
            'tourTitle': '[ %s真實體驗營 ] 腳踏車繞校園＋小木屋鬆餅＋%s鮮奶'%(name, name),
            'tourHour': 3,
            'price': 1000,
            'commentCounter': 3,
            'star': 4,
            'hot': True,
            'recommend': True,
            'categories': ['觀光行程', '一日遊', '美食購物'],
            'image': '0001.jpg'
        }
        trip2 = {
            'tourTitle': '%s風光體驗，湖邊觀景。校內人文介紹與導覽，經驗豐富的學生導遊帶你認識%s'%(name, name),
            'tourHour': 4,
            'price': 800,
            'commentCounter': 0,
            'star': 3,
            'hot': False,
            'recommend': False,
            'categories': ['戶外活動', '自然景觀', '文化藝術'],
            'image': '0002.jpg'
        }
        trip3 = {
            'tourTitle': '%s特色行程與學生最愛的美食！'%(name),
            'tourHour': 2,
            'price': 500,
            'commentCounter': 30,
            'star': 5,
            'hot': True,
            'recommend': True,
            'categories': ['美食購物'],
            'image': '0003.jpg'
        }
        trip4 = {
            'tourTitle': '%s最著名的學生導遊，帶你到別人不知道的私房景點'%(name),
            'tourHour': 5,
            'price': 1200,
            'commentCounter': 2,
            'star': 3,
            'hot': True,
            'recommend': False,
            'categories': ['文化藝術', '觀光行程'],
            'image': '0004.jpg'
        }
        trips = [trip1, trip2, trip3, trip4]
        if 'order' in request.GET and request.GET['order'] != '':
            order = request.GET['order']
            if order == 'hot':
                trips = sorted(trips, key=lambda k: k['hot'], reverse = True)
            elif order == 'price':
                trips = sorted(trips, key=lambda k: k['price'])
            elif order == '-price':
                trips = sorted(trips, key=lambda k: k['price'], reverse = True)
    return  render(request, 'list.html', locals())
