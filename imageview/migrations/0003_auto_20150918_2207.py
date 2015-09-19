# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageview', '0002_auto_20150918_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
