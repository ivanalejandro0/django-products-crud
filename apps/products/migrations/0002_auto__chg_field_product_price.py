# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.price'
        db.alter_column(u'products_product', 'price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Product.price'
        db.alter_column(u'products_product', 'price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2))

    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['products']