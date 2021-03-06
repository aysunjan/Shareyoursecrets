# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secrets_app', '0002_hush'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secrets_app.User')),
                ('likers', models.ManyToManyField(related_name='likedsecrets', to='secrets_app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='hush',
            name='author',
        ),
        migrations.RemoveField(
            model_name='hush',
            name='likers',
        ),
        migrations.DeleteModel(
            name='Hush',
        ),
    ]
