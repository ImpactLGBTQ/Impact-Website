## Widgets file for posting app for impact website
from django import forms
from django.forms import FileInput


## ImageField wrapper which sets required to false and sets up its bootstrap widget classes
class ImageUpload(forms.ImageField):
    widget = FileInput(attrs={'class': 'custom-file-input'})

    def __init__(self, **kwargs):
        if kwargs.get('required'):
            # Remove the required kw if its passed. Bc django forms by default are weird an somewhat evil
            kwargs.pop('required')
        super().__init__(required=False, **kwargs)



