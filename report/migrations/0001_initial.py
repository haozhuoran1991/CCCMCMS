# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='標題', max_length=256)),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容', default='')),
                ('published', models.BooleanField(verbose_name='正式发布', default=True)),
            ],
            options={
                'verbose_name': '報告',
                'verbose_name_plural': '報告',
            },
        ),
    ]
