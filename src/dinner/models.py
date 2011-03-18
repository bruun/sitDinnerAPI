# -*- coding: utf-8 -*-

from django.db import models

class Cafeteria(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    feed = models.URLField()
    

class Dinner(models.Model):
    date = models.DateField()
    cafeteria = models.ForeignKey('Cafeteria', related_name='dinners')
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def __unicode__(self):
        return "%s: %s til %s kroner" % (self.date, self.description, self.price)