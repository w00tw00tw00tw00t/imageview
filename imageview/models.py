import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager


class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    thumbnail = ImageSpecField(source='image_file',
                               processors=[ResizeToFill(100, 100)],
                               format='PNG',
                               options={'quality': 60})
    tags = TaggableManager()
