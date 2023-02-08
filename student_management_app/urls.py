from django.urls import path
from . import views

#
urlpatterns = [
    path('', views.home),
    path('login', views.showLoginPage),
    path('dblogin', views.dbLogin, name='dblogin'),
    path('user_details', views.getUserDetails)
]