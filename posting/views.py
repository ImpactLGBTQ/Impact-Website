import logging

from django.contrib.auth.decorators import login_required
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


@login_required
## Handles request to make a post
class MakeAPostView(View, LoginRequiredMixin):

    ## Handles posting of a new post request
    def post(self, request):
        form = forms.MakeAPostForm(request.POST, request.FILES)

        if form.is_valid():
            form.create_post(request.user)
            # If its a success
            return response.HttpResponseRedirect(reverse_lazy('posting-made-a-post'))
        # An error occured
        errors = form.errors.as_data()
        form.add_error(None, "An error occurred during processing of your request")
        form.add_error(None, errors)
        logging.error("Error occurred when processing of a Make a post form, may be irreversable. Error: {}\nForm: {} "
                      .format(errors, form))
        return render(request, 'posting/make_a_post.html', {'form': form})

    ## Handles the get request, displays the 'make a post' page
    def get(self, request):
        form = forms.MakeAPostForm()
        return render(request, 'posting/make_a_post.html', {'form': form})


class WhatsOnView(View):
    template_name = "posting/posts/whats_on_posts.html"

    ## Handles get request for the page (there is no post request for this page)
    def get(self, request):
        if request.user.is_anonymous:
            # If its an annoymous user, aka not logged in person, set the default 0 access level
            access_level = 0
        else:
            # Else use the users access level
            access_level = request.user.access_level
        cache_query = 'whats_on_recent-{}'.format(access_level)
        # Check the cache for these posts
        cached_posts = cache.get(cache_query)
        if cached_posts:
            posts = cached_posts
            logging.info('Hitting cache for Whats on posts at access level {}'.format(access_level))
        else:
            # Pull first 10 posts
            posts = models.Post.objects.filter(required_access__lte=access_level,
                                               post_type__exact=0).order_by()[:10]
            # Cache the posts
            cache.set(cache_query, posts)
            logging.info("Hitting database and adding to cache for Whats on posts at access level {}".format(access_level))

        return render(request, self.template_name, {'posts': posts})
