# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-23 19:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'updated',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('display_name', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='feedback.Course')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'updated',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_key', models.CharField(db_index=True, max_length=255)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('form_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('post_url', models.URLField()),
                ('submission_url', models.URLField()),
                ('response_msg', models.TextField(blank=True, default=None, null=True, verbose_name='Response')),
                ('response_grade', models.PositiveSmallIntegerField(choices=[(0, 'Rejected'), (1, 'Accepted'), (2, 'Accepted and Good')], default=0, verbose_name='Grade')),
                ('_response_time', models.DateTimeField(db_column='response_time', null=True)),
                ('_response_upl_code', models.PositiveSmallIntegerField(db_column='response_upload_code', default=0)),
                ('_response_upl_attempt', models.PositiveSmallIntegerField(db_column='response_upload_attempt', default=0)),
                ('_response_upl_at', models.DateTimeField(db_column='response_upload_at', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_spec', django.contrib.postgres.fields.jsonb.JSONField()),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='forms', to='feedback.Exercise')),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'updated',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=128)),
                ('full_name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
                'get_latest_by': 'updated',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='form',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='feedbacks', to='feedback.Form'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='feedback.Student'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='superseded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supersedes', to='feedback.Feedback'),
        ),
    ]
