## Forms file for the impact website posting app
from django import forms
from .models import Post
from .widgets import ImageUpload


class MakeAPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'post_type', 'required_access')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        field_classes = {
            'image': ImageUpload,
        }
        labels = {
            'title': 'Title*',
            'content': '',
            'post_type': 'Category',
            'required_access': 'Visibility',
        }
