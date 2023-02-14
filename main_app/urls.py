from django.urls import path
from . import views,adminView, staffView, studentView


#
urlpatterns = [
    path('', views.home),
    path('login', views.showLoginPage, name='login'),
    path('dblogin', views.dbLogin, name='dblogin'),
    path('user_details', views.getUserDetails),
    path('logout_user', views.logout_user, name='logout'),
    path('admin_dashboard', adminView.admin_home, name='admin_dashboard'),
    path('add_staff', adminView.add_staff, name='add_staff'),
    path('add_staff_save', adminView.add_staff_save),
    path('add_department', adminView.add_department, name='add_department'),
    path('add_department_save', adminView.add_department_save),
    path('add_course', adminView.add_course, name='add_course'),
    path('add_student', adminView.add_student, name='add_student'),
    path('add_student_save', adminView.add_student_save),
    path('staff_panel', staffView.staff_panel, name='staff_panel'),
     path('student_panel', studentView.student_panel, name='student_panel'),
     path('view_departments', adminView.view_department),
     path('view_staff', adminView.view_staff),
     path('view_student', adminView.view_student),
     path('view_course', adminView.view_course),
]