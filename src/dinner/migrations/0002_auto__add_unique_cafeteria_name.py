# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Cafeteria', fields ['name']
        db.create_unique('dinner_cafeteria', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Cafeteria', fields ['name']
        db.delete_unique('dinner_cafeteria', ['name'])


    models = {
        'dinner.cafeteria': {
            'Meta': {'object_name': 'Cafeteria'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'dinner.dinner': {
            'Meta': {'object_name': 'Dinner'},
            'cafeteria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dinners'", 'to': "orm['dinner.Cafeteria']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['dinner']
