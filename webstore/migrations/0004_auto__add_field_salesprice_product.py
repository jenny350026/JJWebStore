# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SalesPrice.product'
        db.add_column(u'webstore_salesprice', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['webstore.Product']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SalesPrice.product'
        db.delete_column(u'webstore_salesprice', 'product_id')


    models = {
        u'webstore.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'webstore.inventories': {
            'Meta': {'object_name': 'Inventories'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_in_stock': ('django.db.models.fields.IntegerField', [], {}),
            'num_sold': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.Product']"}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'webstore.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.Product']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2048'})
        },
        u'webstore.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.Category']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'num_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price_purchased': ('django.db.models.fields.IntegerField', [], {}),
            'price_recommended': ('django.db.models.fields.IntegerField', [], {})
        },
        u'webstore.salesprice': {
            'Meta': {'object_name': 'SalesPrice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.Inventories']"}),
            'price_sold': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webstore.Product']"})
        }
    }

    complete_apps = ['webstore']