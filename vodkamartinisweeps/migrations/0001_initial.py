# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sweep'
        db.create_table('vodkamartinisweeps_sweep', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=128)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('source_type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('source_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('brand_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('list_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('vodkamartinisweeps', ['Sweep'])

        # Adding model 'SweepEntry'
        db.create_table('vodkamartinisweeps_sweepentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sweep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vodkamartinisweeps.Sweep'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('gender', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('vodkamartinisweeps', ['SweepEntry'])


    def backwards(self, orm):
        # Deleting model 'Sweep'
        db.delete_table('vodkamartinisweeps_sweep')

        # Deleting model 'SweepEntry'
        db.delete_table('vodkamartinisweeps_sweepentry')


    models = {
        'vodkamartinisweeps.sweep': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Sweep'},
            'brand_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128'}),
            'source_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'source_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'vodkamartinisweeps.sweepentry': {
            'Meta': {'ordering': "['-created']", 'object_name': 'SweepEntry'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'sweep': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vodkamartinisweeps.Sweep']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['vodkamartinisweeps']