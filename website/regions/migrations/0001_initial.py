# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table('regions_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('layer', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('shape', self.gf('django.contrib.gis.db.models.fields.GeometryField')()),
        ))
        db.send_create_signal('regions', ['Region'])

    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table('regions_region')

    models = {
        'regions.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shape': ('django.contrib.gis.db.models.fields.GeometryField', [], {})
        }
    }

    complete_apps = ['regions']