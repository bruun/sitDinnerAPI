"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from dinner.models import Dinner, Cafeteria
from dinner.views import get_dinner_for_day
from django.core.urlresolvers import reverse, resolve

class DinnerTest(TestCase):

    def test_fetching_dinner(self):
        realfag = Cafeteria(name='Realfag', address='Stripa', feed='http://sit.no/rss.ap?thisId=36447&lang=0&ma=on&ti=on&on=on&to=on&fr=on')
        realfag.save()
        #response = self.client.get(reverse(get_dinner_for_day, kwargs={'cafeteria': 'Realfag', 'year': 2011, 'month': 3, 'day': 1}))

        response = self.client.get('/dinner/cafeteria/Realfag/2011/3/7/')
        
        self.failUnlessEqual(response.status_code, 200, "Could not find url, got response code %s" % response.status_code)

        dinners = Dinner.objects.all()
        self.failIfEqual(dinners.count(), 0, 'There should be at least one dinner, but found none')

