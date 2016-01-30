# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160129_1612'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daily_motto',
            options={'verbose_name': '每週背經', 'verbose_name_plural': '每週背經'},
        ),
        migrations.AlterModelOptions(
            name='sundayschool',
            options={'verbose_name': '主日學', 'verbose_name_plural': '主日學'},
        ),
        migrations.AlterField(
            model_name='daily_motto',
            name='motto',
            field=models.TextField(verbose_name='每週選背經文'),
        ),
    ]
