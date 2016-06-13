from django.shortcuts import render
from SATravelWebSystem.views import sessionConnect

# Create your views here.

def guide(request):
    if request.session.get('account', '') != '':
        account = request.session.get('account', '')
        username = sessionConnect(account)
    else:
        username = ''
    return render(request, 'guide.html', locals())
