## Urls file for posting app
from django import urls
from django.urls import path
from . import views

urlpatterns = (
    path('make-a-post', views.MakeAPostView.as_view(), name='posting-make-a-post'),
    path('made-a-post', views.MakeAPostView.as_view(), name='posting-made-a-post'),
    path('whats-on', views.WhatsOnView.as_view(), name='posting-whats-on'),
)

