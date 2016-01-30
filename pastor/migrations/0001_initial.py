# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pastor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=256)),
                ('title', models.CharField(verbose_name='事工方向', max_length=256)),
                ('social_account', models.CharField(default='', verbose_name='社交賬號鏈接', max_length=256)),
                ('intro', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容', default='')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '牧師',
                'verbose_name_plural': '牧師',
            },
        ),
    ]
