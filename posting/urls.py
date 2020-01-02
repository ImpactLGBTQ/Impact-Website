## Urls file for posting app
from django import urls
from django.urls import path
from . import views

urlpatterns = (
    path('make-a-post', views.MakeAPostView.as_view(), name='posting:make-a-post'),
    path('made-a-post', name='posting:made-a-post'),

)

