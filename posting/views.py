from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import response
from django.views import View
from . import forms
from . import models
import datetime


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
            access_level = data['required_access']
            p_type = data['post_type']

            # Add the post to the database and return
            post = models.Post(author=author, title=title, content=content, image=img, required_access=access_level,
                               post_type=p_type)
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


class WhatsOnView(View):
    template_name = "posting/posts/whats_on_posts.html"

    ## Handles get request for the page (there is no post request for this page)
    def get(self, request):
        cache_query = 'whats_on_recent-{}'.format(request.user.access_level)
        # Check the cache for these posts
        cached_posts = cache.get(cache_query)
        if cached_posts:
            posts = cached_posts
        else:
            # Pull first 10 posts
            posts = models.Post.objects.filter(required_access__lte=request.user.access_level,
                                               post_type__exact=0).order_by()[:10]
            # Cache the posts
            cache.set(cache_query, posts)

        return render(request, self.template_name, {'posts': posts})
