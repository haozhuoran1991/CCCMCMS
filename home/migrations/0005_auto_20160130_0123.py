# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160129_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='sundayschool',
            name='teacher',
            field=models.CharField(verbose_name='主講人', max_length=256, default=datetime.datetime(2016, 1, 30, 7, 23, 0, 570927, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='daily_motto',
            name='motto',
            field=models.TextField(unique=True, verbose_name='每週選背經文', default='耶和華賜人智慧，知識和聰明都由祂口'),
        ),
    ]
