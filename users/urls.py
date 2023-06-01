from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
    path('info', views.SingleUserView.as_view(), name='single_user'),
    path('login', views.UserLoginView.as_view(), name='user_login'),
    path('logout', views.UserLogoutView.as_view(), name='user_logout'),
]
