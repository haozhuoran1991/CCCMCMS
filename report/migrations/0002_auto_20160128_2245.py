# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 29, 4, 45, 4, 149201, tzinfo=utc), verbose_name='发表时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True),
        ),
    ]
