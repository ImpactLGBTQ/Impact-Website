## Forms file for the impact website posting app
from django.forms import forms, ModelForm
from .models import Post


class MakeAPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
