## Forms file for the impact website posting app
from django.forms import forms, ModelForm, TextInput, Textarea, FileInput
from .models import Post


class MakeAPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'custom-file-input'}),
        }
        labels = {
            'title': 'Title*',
            'content': '',
        }