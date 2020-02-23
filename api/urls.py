from django.urls import path

from . import views

app_name = 'api'
urlpatterns = (
    path('logmein/', views.AuthenticateUser.as_view, name='authenticate-user'),

)


