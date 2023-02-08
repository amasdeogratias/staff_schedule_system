from django.urls import path
from . import views
from . import adminView

#
urlpatterns = [
    path('', views.home),
    path('login', views.showLoginPage),
    path('dblogin', views.dbLogin, name='dblogin'),
    path('user_details', views.getUserDetails),
    path('logout_user', views.logout_user, name='logout'),
    path('admin_home', adminView.admin_home, name='admin_home')
]