from django.contrib.auth.views import LogoutView
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
import posting.models as posting_models
from .serializers import UserSerializer, PostSerializer
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django import http
import json
import logging
from .responses import HttpResponseUnauthorized


# Create your views here.

# Authentcation and sign in a user
class AuthenticateUser(ObtainAuthToken):
    def post(self, request, **kwargs):
        json_data = request.body
        print("Recived: ", json_data)

        try:
            data = json.loads(json_data)
        except TypeError:
            logging.debug("Failed to decode json data. RAW: {}".format(json_data))
            return http.HttpResponseBadRequest()

        # Data has been parsed successfully

        # Unpack the data
        username = data['username']
        password = data['password']

        # Test login
        user = authenticate(username=username, password=password)

        if user:
            # Logged in successfully
            # Get the token
            token = Token.objects.get(user=user)
            return http.JsonResponse({"token": token.key})

        return HttpResponseUnauthorized()

# 'Delete' a post 
class DelPost(APIView):

    def get(self, request, post_id):
        # If anonymous definitely forbidden
        if request.user.is_anonymous:
            return http.HttpResponseForbidden()

        post = posting_models.Post.objects.get(uuid__exact=post_id)
        if post.author != request.user and request.user.access_level < 2:
            # Not staff and not owner of the post
            return http.HttpResponseForbidden()
        # User is valid and can delete this post

        # Hide it, effectively deleting it
        post.is_visible = False

        # Save changes
        post.save()

        # Return success
        return http.HttpResponse()

# Get a specified (up to 20) number of posts 
class GetPosts(APIView):
    authentication_classes = []

    def get(self, request, num):
        # Ensure not too big
        if num < 1 or num > 20:
            return http.HttpResponseBadRequest()

        if request.user.is_anonymous:
            # If its an annoymous user, aka not logged in person, set the default 0 access level
            access_level = 0
        else:
            # Else use the users access level
            # Ensure access level is updated
            request.user.sync_access_level()
            access_level = request.user.access_level
        cache_query = 'whats_on_recent-{}'.format(access_level)
        # Check the cache for these posts
        cached_posts = cache.get(cache_query)
        if cached_posts:
            posts = cached_posts
            logging.info('Hitting cache for Whats on posts at access level {}'.format(access_level))
        else:
            # Pull first 10 posts
            posts = posting_models.Post.objects.filter(required_access__lte=access_level,
                                                       post_type__exact=0, is_visible=True).order_by()[:10]
            # Cache the posts
            cache.set(cache_query, posts)
            logging.info(
                "Hitting database and adding to cache for Whats on posts at access level {}".format(access_level))

        serialized = PostSerializer(posts, many=True)
        return http.JsonResponse(serialized.data, safe=False)


# Adds a post to the database, also returns the details of the added post
class AddPost(APIView):

    def post(self, request):
        # Require login
        if request.user.is_anonymous:
            return http.HttpResponseForbidden()

        # Get the raw data
        print('Got: ', request.body)
        try:
            json_raw = json.loads(request.body)
        except json.JSONDecodeError as e:
            logging.exception("Failed to decode message: "+request.body+" error: "+str(e))
        post = posting_models.Post(title=json_raw['title'], content=json_raw['content'], author=request.user,
                                   post_type=json_raw['type'], required_access=json_raw['access_level'])
        post.save()

        post_info = {"uuid": post.uuid}

        return http.JsonResponse(json.dumps(post_info), safe=False)

# Get a csrf token
class GetCSRF(APIView):

    def get(self, request, **kw):
        return render(request, 'api/get_csrf.html')

# Get information about the currently signed in user
class GetUserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Log the current user out
class DeauthUser(LogoutView, APIView):
    pass
