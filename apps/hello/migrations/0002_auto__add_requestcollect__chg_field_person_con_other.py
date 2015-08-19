# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestCollect'
        db.create_table(u'hello_requestcollect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('r_method', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('r_path', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('r_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('r_read_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'hello', ['RequestCollect'])


        # Changing field 'Person.con_other'
        db.alter_column(u'hello_person', 'con_other', self.gf('django.db.models.fields.TextField')(max_length=400))

    def backwards(self, orm):
        # Deleting model 'RequestCollect'
        db.delete_table(u'hello_requestcollect')


        # Changing field 'Person.con_other'
        db.alter_column(u'hello_person', 'con_other', self.gf('django.db.models.fields.TextField')(max_length=79))

    models = {
        u'hello.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'con_email': ('django.db.models.fields.EmailField', [], {'max_length': '79'}),
            'con_jabbber': ('django.db.models.fields.EmailField', [], {'max_length': '79'}),
            'con_other': ('django.db.models.fields.TextField', [], {'max_length': '400', 'blank': 'True'}),
            'con_skype': ('django.db.models.fields.CharField', [], {'max_length': '79'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'hello.requestcollect': {
            'Meta': {'object_name': 'RequestCollect'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'r_method': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'r_path': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'r_read_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'r_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']