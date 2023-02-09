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
    path('admin_dashboard', adminView.admin_home, name='admin_dashboard'),
    path('add_staff', adminView.add_staff, name='add_staff'),
    path('add_staff_save', adminView.add_staff_save)
]