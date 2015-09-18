import os
from PIL import Image
from io import BytesIO

from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your models here.
class Imageview(models.Model):
    imagefile = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='images/thumbnails/')
    
    def create_thumbnail(self):
        if not self.image:
            return
        readimage = BytesIO(self.image.read())
        orginal_image = Image.open(readimage)
        new_image = orginal_image.copy()
        
        new_image.thumbnail( (100,100) , Image.ANTIALIAS ) 
        
        temp_handle = BytesIO()
        new_image.save( temp_handle, 'png' )
        temp_handle.seek(0)
        
        fn = os.path.split(self.image.name)[-1]
        suf = SimpleUploadedFile( fn , temp_handle.read() , content_type='png' )
        self.thumbnail.save('%s_thumbnail.%s' % ( fn , 'png' ) , suf , save=False )
    def save(self):
        self.create_thumbnail()
        
        super(Imageview,self).save()

class Imagetag(models.Model):
    name   = models.CharField(maxlen=100)
    images = models.ManyToMany(Imageview)
    
