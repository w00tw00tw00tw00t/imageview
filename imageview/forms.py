from django.forms import ModelForm
from .models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'description', 'image_file', 'tags')
        labels = {
                     'image_file': 'Select an Image',
                 },
        help_texts = {
            'image_file': 'Max. 42 megabytes.'
        }
