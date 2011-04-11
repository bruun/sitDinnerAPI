# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Cafeteria'
        db.create_table('dinner_cafeteria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('feed', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('dinner', ['Cafeteria'])

        # Adding model 'Dinner'
        db.create_table('dinner_dinner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('cafeteria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dinners', to=orm['dinner.Cafeteria'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dinner', ['Dinner'])


    def backwards(self, orm):
        
        # Deleting model 'Cafeteria'
        db.delete_table('dinner_cafeteria')

        # Deleting model 'Dinner'
        db.delete_table('dinner_dinner')


    models = {
        'dinner.cafeteria': {
            'Meta': {'object_name': 'Cafeteria'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
