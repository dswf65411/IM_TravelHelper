from django.shortcuts import render
from SATravelWebSystem.views import sessionConnect, graceful_auto_reconnect

# Create your views here.

def guide(request):
    if request.session.get('account', '') != '':
        account = request.session.get('account', '')
        username = graceful_auto_reconnect(sessionConnect(account))
    else:
        username = ''
    return render(request, 'guide.html', locals())
