# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Dinner.description'
        db.alter_column('dinner_dinner', 'description', self.gf('django.db.models.fields.CharField')(max_length=1000))


    def backwards(self, orm):
        
        # Changing field 'Dinner.description'
        db.alter_column('dinner_dinner', 'description', self.gf('django.db.models.fields.CharField')(max_length=100))


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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['dinner']
