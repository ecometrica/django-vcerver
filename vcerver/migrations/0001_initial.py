# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('vcerver_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('card_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('local_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('_firstname', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('_lastname', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('personnal_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vcerver.Address'], null=True, blank=True)),
            ('work', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vcerver.Company'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('vcerver', ['Contact'])

        # Adding model 'Company'
        db.create_table('vcerver_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vcerver.Address'], null=True, blank=True)),
        ))
        db.send_create_signal('vcerver', ['Company'])

        # Adding model 'Address'
        db.create_table('vcerver_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
        ))
        db.send_create_signal('vcerver', ['Address'])

        # Adding model 'URL'
        db.create_table('vcerver_url', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vcerver.Contact'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('explicit_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('vcerver', ['URL'])


    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('vcerver_contact')

        # Deleting model 'Company'
        db.delete_table('vcerver_company')

        # Deleting model 'Address'
        db.delete_table('vcerver_address')

        # Deleting model 'URL'
        db.delete_table('vcerver_url')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'vcerver.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        'vcerver.company': {
            'Meta': {'object_name': 'Company'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vcerver.Address']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'vcerver.contact': {
            'Meta': {'object_name': 'Contact'},
            '_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            '_firstname': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            '_lastname': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'card_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'personnal_address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vcerver.Address']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vcerver.Company']", 'null': 'True', 'blank': 'True'})
        },
        'vcerver.url': {
            'Meta': {'object_name': 'URL'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['vcerver.Contact']"}),
            'explicit_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'})
        }
    }

    complete_apps = ['vcerver']
