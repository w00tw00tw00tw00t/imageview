# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imageview.storage
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('imageview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='md5sum',
            field=models.CharField(unique=True, default=datetime.datetime(2015, 9, 19, 2, 24, 57, 24199, tzinfo=utc), max_length=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.TextField(unique=True, default=datetime.datetime(2015, 9, 19, 2, 25, 0, 230147, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to=imageview.storage.media_file_name, storage=imageview.storage.MediaFileSystemStorage()),
        ),
    ]
