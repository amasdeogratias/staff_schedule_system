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
    
    # paths for staffs
    path('add_staff', adminView.add_staff, name='add_staff'),
    path('add_staff_save', adminView.add_staff_save, name='add_staff_save'),
    path('staff_panel', staffView.staff_panel, name='staff_panel'),
     path('view_staff', adminView.view_staff, name='view_staff'),
    
    # paths for departments
    path('add_department', adminView.add_department, name='add_department'),
    path('add_department_save', adminView.add_department_save, name='add_department_save'),
    path('view_departments', adminView.view_department, name='view_departments'),
    path('edit_department/<str:department_id>', adminView.edit_department, name='edit_department'),
    path('edit_department_save', adminView.edit_department_save, name='edit_department_save'),
    
    # paths for courses
    path('add_course', adminView.add_course, name='add_course'),
    path('add_course_save', adminView.add_course_save, name='add_course_save'),
    path('view_course', adminView.view_course, name='view_course'),
    
    
    # paths for students
    path('add_student', adminView.add_student, name='add_student'),
    path('add_student_save', adminView.add_student_save, name='add_student_save'),   
    path('student_panel', studentView.student_panel, name='student_panel'), 
    path('view_student', adminView.view_student, name='view_student'),
    path('edit_course/<str:course_id>', adminView.edit_course, name='edit_course'),
    
     
     
]