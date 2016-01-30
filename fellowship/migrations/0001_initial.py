# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fellowship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='團契名稱', max_length=256)),
                ('slug', models.CharField(db_index=True, verbose_name='團契网址', max_length=256)),
                ('intro', DjangoUeditor.models.UEditorField(blank=True, verbose_name='團契簡介', default='')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '團契',
                'verbose_name_plural': '團契',
            },
        ),
    ]
