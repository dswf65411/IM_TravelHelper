from django.shortcuts import render
from mongoDB.connection import connect

# Create your views here.

def trip(request):
    if 'region' in request.GET and request.GET['region'] != '':
        if 'school' in request.GET and request.GET['school'] != '':
            if 'tripID' in request.GET and request.GET['tripID'] != '':
                region = request.GET['region']
                school = request.GET['school']
                tripID = int(request.GET['tripID'])
                trip = tripConnect(region, school, tripID)
                sites = trip['site']
                comments = trip['comments']
    return render(request, 'trip.html', locals())

def tripConnect(region, school, tripID):
    DB = connect()
    collect = DB[region]
    temp = collect.find({'name': school },{'trip':1,'_id':0})[0]['trip']
    trip = temp[tripID-1]
    countingStar = 0
    for count in trip['star']:
        countingStar += count['score']
    trip['star']=int(countingStar/len(trip['star']))
    return trip
