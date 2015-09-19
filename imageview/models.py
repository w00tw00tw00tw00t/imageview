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

    def image_tag(self):
        return u'<img src="%s" />' % self.thumbnail.url

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.image_file.name.split('/')[-1]
