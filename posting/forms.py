## Forms file for the impact website posting app
from django.forms import forms, ModelForm, TextInput, Textarea, ImageField, FileInput
from .models import Post
from .widgets import ImageUpload


class MakeAPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'post_type', 'required_access')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
        }
        field_classes = {
            'image': ImageUpload,
        }
        labels = {
            'title': 'Title*',
            'content': '',
        }