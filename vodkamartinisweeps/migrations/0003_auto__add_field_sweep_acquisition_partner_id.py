# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sweep.acquisition_partner_id'
        db.add_column('vodkamartinisweeps_sweep', 'acquisition_partner_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sweep.acquisition_partner_id'
        db.delete_column('vodkamartinisweeps_sweep', 'acquisition_partner_id')


    models = {
        'vodkamartinisweeps.sweep': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Sweep'},
            'acquisition_partner_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
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
            'receive_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sweep': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vodkamartinisweeps.Sweep']"}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['vodkamartinisweeps']