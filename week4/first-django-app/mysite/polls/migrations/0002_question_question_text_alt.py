# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text_alt',
            field=models.CharField(default='stuff', max_length=200),
        ),
    ]
