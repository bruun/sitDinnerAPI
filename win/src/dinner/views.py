import urllib2
import re
import time

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from dinner.models import Cafeteria, Dinner
from datetime import date, timedelta


def get_dinner(request, cafeteria, year, month, day):
    """
        Fetches the dinner for the requested day of the week.
        If the dinner is not previously fetched, it will fetch from sit.no

    """
    cafeteria = get_object_or_404(Cafeteria, name=cafeteria)
    today = date(int(year), int(month), int(day))
    if today.weekday() not in range(5):
        return HttpResponse('helg')
    
    # First check if we already fetched and saved the dinners
    if Dinner.objects.filter(cafeteria=cafeteria, date=today).count() == 0:
        # Try to fetch dinners from the SiT website
        # @TODO check if the date specified is in this week, if not there is no use trying to fetch dinner
        fetch_and_create(cafeteria, today)
    dinners = Dinner.objects.filter(cafeteria=cafeteria, date=today)
    if not dinners:
        # No dinners, sowwy
        return HttpResponse("fant nada")
    
    return HttpResponse(dinners)


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
                        r2 = re.match(u'\s*(.*?):\s*(\d+)', item)
                        if r2 != None:
                            food, price = r2.groups()
                            #print food
                            menu[day].append({food: price})

                            #print '%s Pris: %s' % (food, price)
                    counter = counter + 1

        r2 = re.compile(u'Uke.(\d+)', re.S)
        result2 = r2.search(p)

        if result2:
            try:
                week = int(result2.group(1))
            except:
                week = 0

            if week <= 52 and week >= 1:

                for day in menu:
                    print day

                    today = date.fromtimestamp(time.mktime(time.strptime('%d %d %d'  % (date.today().year, week, weekdays[day]) , '%Y %W %w')))

                    for item in menu[day]:
                        for food, price in item.iteritems():
                            Dinner.objects.create(cafeteria=cafeteria, description=food, price=price, date=today)
                            #print "         %s: %s til %s kroner" % (today, food, price)
    return