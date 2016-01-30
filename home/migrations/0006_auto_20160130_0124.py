# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160130_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sundayschool',
            name='teacher',
            field=models.CharField(max_length=256, verbose_name='主講人', default=''),
        ),
    ]
