from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from . import forms
from . import models
# Create your views here.


## Handles request to make a post
class MakeAPostView(View, LoginRequiredMixin):

    ## Handles posting of a new post request
    def post(self, request):
        form = forms.MakeAPostForm(request.POST)

        if form.is_valid():
            # If the form is a valid post

            # Set author
            author = request.user

            # Pull out the data
            data = form.cleaned_data
            title = data['title']
            content = data['content']
            img = data['image']

            # Add the post to the database and return
            post = models.Post(author=author, title=title, content=content, image=img)
            if post.save():
                # If its a success
                return reverse_lazy('posting:made-a-post')



