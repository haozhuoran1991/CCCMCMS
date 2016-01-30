# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='daily_motto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('motto', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)),
            ],
        ),
    ]
