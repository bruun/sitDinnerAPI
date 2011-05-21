# -*- coding: utf-8 -*-

import urllib2
import re
import time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils import simplejson as json

from dinner.models import Cafeteria, Dinner
from datetime import date, timedelta

def get_cafeterias(request):
    
    data = serializers.serialize('json', Cafeteria.objects.all(),
                                 fields=('name', 'address'), ensure_ascii=False)
    return HttpResponse(data)

def get_dinner_for_today(request, cafeteria):
    today = date.today()
    return get_dinner_for_day(request, cafeteria, today.year, today.month, today.day)


def get_dinner_for_day(request, cafeteria, year, month, day):
    """
        Fetches the dinner for the requested day of the week.
        If the dinner is not previously fetched, it will fetch from sit.no

    """
    error = []
    cafeteria = get_object_or_404(Cafeteria, name=cafeteria)
    today = date(int(year), int(month), int(day))
    if today.weekday() not in range(5):
        error = json.dumps([{'error': {'type':'weekend', 'message': 'Det er helg!'}}])
        return HttpResponse(error)
    # First check if we already fetched and saved the dinners
    if Dinner.objects.filter(cafeteria=cafeteria, date=today).count() == 0:
        # Try to fetch dinners from the SiT website
        # @TODO check if the date specified is in this week, if not there is no use trying to fetch dinner
        fetch_and_create(cafeteria, today)
    
    dinners = Dinner.objects.filter(cafeteria=cafeteria, date=today)
    if not dinners:
        if cafeteria.name == 'Moholt':
            error = json.dumps([{'error': {'type':'unsupported', 'message': 'Beklager, Moholt er foreløpig ikke støttet.'}}], ensure_ascii=False)
        else:
            # No dinners, sowwy
            error = json.dumps([{'error': {'type':'weekend', 'message': 'Ingen måltider funnet!'}}], ensure_ascii=False)
        return HttpResponse(error)
    
    
    data = serializers.serialize('json', dinners, ensure_ascii=False, use_natural_keys=True)
    return HttpResponse(data)

def get_dinner_for_this_week(request, cafeteria):
    today = date.today()
    return get_dinner_for_week_by_day(request, cafeteria, today.year, today.month, today.day)

def get_dinner_for_week_by_day(request, cafeteria, year, month, day):
    """
        Fetches the dinner for the requested day of the week.
        If the dinner is not previously fetched, it will fetch from sit.no

    """
    weekdays = {0:"Mandag",
                1:"Tirsdag",
                2:"Onsdag",
                3:"Torsdag",
                4:"Fredag",}

    cafeteria = get_object_or_404(Cafeteria, name=cafeteria)
    today = date(int(year), int(month), int(day))
    weekday = today.weekday()


    if weekday not in range(5):
        error = json.dumps([{"Weekend": [{"error": "Det er helg!"}]}])
        return HttpResponse(error)
    
    # First check if we already fetched and saved the dinners
    if Dinner.objects.filter(cafeteria=cafeteria, date=today).count() == 0:
        # Try to fetch dinners from the SiT website
        # Check if the date specified is in this week, if not there is no use trying to fetch dinner
        if today.isocalendar()[1] == date.today().isocalendar()[1]:
            fetch_and_create(cafeteria, today)
            print "Fetching"

    week_dinners = []
    # Fetch dinners by days remaining that week
    for w in range(5-weekday):

        daily_dinners = Dinner.objects.filter(cafeteria=cafeteria, date=today)
        if not daily_dinners:
            # No dinners, sorry... 
            error = [{'error': u"Ingen måltider funnet!"}]
            week_dinners.append({weekdays[today.weekday()]: error})
        else:
            # Manually serialize (*sigh*) the queryset
            
            dinners_serialized = []
            for dinner in daily_dinners:
                dinners_serialized.append({
                    "date": "%s" % dinner.date,
                    "price": "%s" % dinner.price,
                    "cafeteria": "%s" % dinner.cafeteria.name,
                    "description": "%s" % dinner.description
                })
            week_dinners.append({weekdays[today.weekday()]: dinners_serialized})
        today = today + timedelta(days=1)
    return HttpResponse(json.dumps(week_dinners, ensure_ascii=False))

def fetch_and_create(cafeteria, date):
    menu = {'Mandag':[],
            'Tirsdag':[],
            'Onsdag':[],
            'Torsdag':[],
            'Fredag':[]}

    weekdays = {'Mandag':1,
                'Tirsdag':2,
                'Onsdag':3,
                'Torsdag':4,
                'Fredag':5}
    try:
        p = urllib2.urlopen(cafeteria.feed, timeout=5).read().decode('utf-8')
        #p = urllib2.urlopen('http://sit.no/rss.ap?thisId=36447&lang=0&ma=on&ti=on&on=on&to=on&fr=on', timeout=5).read().decode('utf-8')
    except urllib2.HTTPError, e:
        print e.code
        print e.msg
        print e.headers
        print e.fp.read()
    
    except urllib2.URLError, e:
        print e
    else:
        for day in menu:
            #print day
            r1 = re.compile(u'<b>%s:</b>(?:\s*\W+\s*)(.*?)(?:<br>\s*<br>)' % day, re.S)
            result1 = r1.search(p)
            if result1:
                contents = result1.group(1)
                #print contents

                content_list = contents.split('br>')
                counter = 0
                for item in content_list:
                    if item != '':
                        r2 = re.match(u'\s*(.*?):\s*\D*(\d+)', item)
                        if r2 != None:
                            food, price = r2.groups()
                            #print food
                            menu[day].append({food: price})

                            #print '%s Pris: %s' % (food, price)
                    counter = counter + 1

        for day in menu:
            #print day
            # Iso week number
            week = date.isocalendar()[1]
            today = date.fromtimestamp(time.mktime(time.strptime('%d %d %d'  % (date.today().year, week, weekdays[day]) , '%Y %W %w')))
            for item in menu[day]:
                for food, price in item.iteritems():
                    Dinner.objects.get_or_create(cafeteria=cafeteria, description=food, price=price, date=today)
                    #print u"         %s: %s til %s kroner" % (today, food, price)
    return


def delete_future():
    future = Dinner.objects.filter(date__gt=date.today())
    for f in future:
        f.delete()