# -*- coding: utf-8 -*-

from django.db import models


class Cafeteria(models.Model):

    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    feed = models.URLField()

    def natural_key(self):
        return (self.name)

class Dinner(models.Model):


    date = models.DateField()
    cafeteria = models.ForeignKey('Cafeteria', related_name='dinners')
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def __unicode__(self):
        return "%s: %s til %s kroner" % (self.date, self.description, self.price)



def initial_data():
    
    Cafeteria.objects.get_or_create(name='Hangaren',
                                    address='Enden av Stripa, sør for Sentralbygg 1, Gløshaugen',
                                    feed='http://sit.no/rss.ap?thisId=36444&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Realfag',
                                    address='Realfagbygget, Gløshaugen',
                                    feed='http://sit.no/rss.ap?thisId=36447&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Dragvoll',
                                    address='Bygg 5, nivå 4',
                                    feed='http://sit.no/rss.ap?thisId=36441&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Tyholt',
                                    address='Marinteknisk senter, Tyholt',
                                    feed='http://sit.no/rss.ap?thisId=36450&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Kalvskinnet',
                                    address='Gunnerusgt 1',
                                    feed='http://sit.no/rss.ap?thisId=36453&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Moholt',
                                    address='Trondheim Økonomiske Høgskole',
                                    feed='http://sit.no/rss.ap?thisId=36456&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Ranheimsveien',
                                    address='Radmannbygget, Leangen',
                                    feed='http://sit.no/rss.ap?thisId=38753&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Rotvoll',
                                    address='Rotvoll',
                                    feed='http://sit.no/rss.ap?thisId=38910&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='DMMH',
                                    address='Dalen, ved KBS kjøpesenter',
                                    feed='http://sit.no/rss.ap?thisId=38798&lang=0&ma=on&ti=on&on=on&to=on&fr=on')

    Cafeteria.objects.get_or_create(name='Oya',
                                    address='',
                                    feed='http://sit.no/rss.ap?thisId=37228&lang=0&ma=on&ti=on&on=on&to=on&fr=on')
    Cafeteria.objects.get_or_create(name='Elektro',
                                    address='',
                                    feed='http://sit.no/rss.ap?thisId=40227&lang=0&ma=on&ti=on&on=on&to=on&fr=on')
