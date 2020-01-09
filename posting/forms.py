## Forms file for the impact website posting app
import logging

from django import forms
from django.core.cache import cache

from .models import Post, User
from .widgets import ImageUpload


class MakeAPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'post_type', 'required_access')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'post_type': forms.Select(attrs={'class': 'custom-select'}),
            'required_access': forms.Select(attrs={'class': 'custom-select'}),
        }
        field_classes = {
            'image': ImageUpload,
        }
        labels = {
            'title': 'Post title',
            'content': '',
            'post_type': 'Category',
            'required_access': 'Visibility',
            'image': ' '
        }

    def create_post(self, author: User):
        # Pull out the data
        data = self.cleaned_data
        title = data['title']
        content = data['content']
        img = data['image']
        access_level = data['required_access']
        p_type = data['post_type']

        # Add the post to the database and return
        post = Post(author=author, title=title, content=content, image=img, required_access=access_level,
                    post_type=p_type)
        post.save()
        # Delete all the cache for posts up to our access level
        cache.delete_many(['whats_on_recent-{}'.format(x) for x in range(0, access_level)])
        logging.info("{} made a post with access level: {}".format(author, access_level))

