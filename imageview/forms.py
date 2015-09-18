from django import forms

class ImageviewForm(forms.Form):
    imagefile = forms.ImageField(
        label='Select an image',
        help_text='max. 42 megabytes'
    )