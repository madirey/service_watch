# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('servicewatch_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('servicewatch', ['Tag'])

        # Adding field 'Grower.name'
        db.add_column('servicewatch_grower', 'name',
                      self.gf('django.db.models.fields.CharField')(default='stupid', max_length=40),
                      keep_default=False)

        # Adding M2M table for field skills on 'Grower'
        db.create_table('servicewatch_grower_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('grower', models.ForeignKey(orm['servicewatch.grower'], null=False)),
            ('tag', models.ForeignKey(orm['servicewatch.tag'], null=False))
        ))
        db.create_unique('servicewatch_grower_skills', ['grower_id', 'tag_id'])

        # Adding M2M table for field interests on 'Grower'
        db.create_table('servicewatch_grower_interests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('grower', models.ForeignKey(orm['servicewatch.grower'], null=False)),
            ('tag', models.ForeignKey(orm['servicewatch.tag'], null=False))
        ))
        db.create_unique('servicewatch_grower_interests', ['grower_id', 'tag_id'])

    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('servicewatch_tag')

        # Deleting field 'Grower.name'
        db.delete_column('servicewatch_grower', 'name')

        # Removing M2M table for field skills on 'Grower'
        db.delete_table('servicewatch_grower_skills')

        # Removing M2M table for field interests on 'Grower'
        db.delete_table('servicewatch_grower_interests')

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
        'servicewatch.grower': {
            'Meta': {'object_name': 'Grower'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'interests_growers'", 'symmetrical': 'False', 'to': "orm['servicewatch.Tag']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'skills_growers'", 'symmetrical': 'False', 'to': "orm['servicewatch.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'servicewatch.sower': {
            'Meta': {'object_name': 'Sower'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'You need a title'", 'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'servicewatch.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'servicewatch.task': {
            'Meta': {'object_name': 'Task'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['servicewatch']