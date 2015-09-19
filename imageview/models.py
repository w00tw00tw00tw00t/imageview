from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from hashlib import md5
from .storage import MediaFileSystemStorage, media_file_name
from django.core.exceptions import ValidationError


class Image(models.Model):
    image_file = models.ImageField(upload_to=media_file_name, storage=MediaFileSystemStorage())
    thumbnail = ImageSpecField(source='image_file',
                               processors=[ResizeToFill(100, 100)],
                               format='PNG',
                               options={'quality': 60})
    tags = TaggableManager()
    title = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=True)
    md5sum = models.CharField(max_length=36, unique=True)

    def clean(self):
        if not self.pk:
            _md5 = md5()
            for chunk in self.image_file.chunks():
                _md5.update(chunk)
            self.md5sum = _md5.hexdigest()

            check_md5 = Image.objects.filter(md5sum=self.md5sum)

            if check_md5:
                raise ValidationError({'image_file': "Image has already been uploaded."})

    def image_tag(self):
        # noinspection PyUnresolvedReferences
        return u'<a href="%s" target="_blank"><img src="%s" /></a>' % (self.image_file.url, self.thumbnail.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.image_file.name
