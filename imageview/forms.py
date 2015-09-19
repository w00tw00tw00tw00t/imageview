from django.forms import ModelForm
from taggit.forms import TagField
from .models import Image
# import taggit_bootstrap


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

        # widgets = {
        #     'tags': TagField(widget=taggit_bootstrap.TagsInput, show_hidden_initial=True)
        # }
        #
        #
        # tags=TagField(widget=taggit_bootstrap.TagsInput)
        #
