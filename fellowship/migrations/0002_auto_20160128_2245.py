# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fellowship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellowship',
            name='slug',
            field=models.CharField(db_index=True, verbose_name='團契网址', max_length=256, unique=True),
        ),
    ]
