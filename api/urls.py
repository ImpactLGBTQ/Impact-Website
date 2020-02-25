from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'api'
urlpatterns = (
    path('csrf/', views.GetCSRF.as_view(), name='get-csrf'),
    path('user/', views.GetUserInfo.as_view(), name="get-user-info"),

    path('posting/get/<int:num>', views.GetPosts.as_view(), name='get-posts'),
    path('posting/new/', views.AddPost.as_view(), name='new-post'),
    path('post/del/<uuid:post_id>', views.DelPost.as_view(), name='del-post'),

    path('auth/logmein/', views.AuthenticateUser.as_view(), name='authenticate-user'),
    path('auth/logmeout/', views.LogoutView.as_view(), name='logout-user'),
)


