from django import urls
from django.urls import path
from . import views

# urls python file for the impact_forum app


urlpatterns = (
    path('', views.homepage, name='impact_website-homepage'),
)
