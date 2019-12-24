from django import urls
from django.urls import path
from . import views

# urls python file for the impact_forum app


urlpatterns = (
    path('', views.homepage),
    path('home', views.homepage,  name='impact_website-homepage'),
    path('about-us', views.about_us, name='impact_website-about-us'),
    path('signposting', views.signposting, name='impact_website-signposting'),
)
