# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_daily_motto'),
    ]

    operations = [
        migrations.CreateModel(
            name='SundaySchool',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='課程名字', max_length=256)),
                ('classroom', models.CharField(verbose_name='教室', max_length=256)),
                ('intro', models.TextField(verbose_name='課程簡介')),
            ],
        ),
        migrations.AlterField(
            model_name='daily_motto',
            name='motto',
            field=models.CharField(verbose_name='每週選背經文', max_length=256),
        ),
    ]
