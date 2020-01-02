from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import response
from django.views import View
from . import forms
from . import models
# Create your views here.


## Handles request to make a post
class MakeAPostView(View, LoginRequiredMixin):

    ## Handles posting of a new post request
    def post(self, request):
        form = forms.MakeAPostForm(request.POST, request.FILES)

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
            post.save()
            # If its a success
            return response.HttpResponseRedirect(reverse_lazy('posting-made-a-post'))
        # An error occured
        errors = form.errors.as_data()
        form.add_error(None, "An error occurred during processing of your request")
        form.add_error(None, errors)
        return render(request, 'posting/make_a_post.html', {'form': form})

    ## Handles the get request, displays the 'make a post' page
    def get(self, request):
        form = forms.MakeAPostForm()
        return render(request, 'posting/make_a_post.html', {'form': form})


