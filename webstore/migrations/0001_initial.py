# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'webstore_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'webstore', ['Category'])

        # Adding model 'Product'
        db.create_table(u'webstore_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.Category'])),
            ('price_purchased', self.gf('django.db.models.fields.IntegerField')()),
            ('price_recommended', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('num_views', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'webstore', ['Product'])

        # Adding model 'Inventories'
        db.create_table(u'webstore_inventories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.Product'])),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('num_in_stock', self.gf('django.db.models.fields.IntegerField')()),
            ('num_sold', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'webstore', ['Inventories'])

        # Adding model 'Picture'
        db.create_table(u'webstore_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.Product'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=2048)),
        ))
        db.send_create_signal(u'webstore', ['Picture'])

        # Adding model 'SalesPrice'
        db.create_table(u'webstore_salesprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.Product'])),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webstore.Inventories'])),
            ('price_sold', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'webstore', ['SalesPrice'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'webstore_category')

        # Deleting model 'Product'
        db.delete_table(u'webstore_product')

        # Deleting model 'Inventories'
        db.delete_table(u'webstore_inventories')

        # Deleting model 'Picture'
        db.delete_table(u'webstore_picture')

        # Deleting model 'SalesPrice'
        db.delete_table(u'webstore_salesprice')


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