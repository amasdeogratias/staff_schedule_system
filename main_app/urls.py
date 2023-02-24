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
    path('admin_profile', adminView.admin_profile, name="admin_profile"),
    path('admin_profile_save', adminView.admin_profile_save, name="admin_profile_save"),
    
    # paths for staffs
    path('add_staff', adminView.add_staff, name='add_staff'),
    path('add_staff_save', adminView.add_staff_save, name='add_staff_save'),
    path('staff_panel', staffView.staff_panel, name='staff_panel'),
    path('view_staff', adminView.view_staff, name='view_staff'),
    path('edit_staff/<str:staff_id>', adminView.edit_staff, name='edit_staff'),
    path('edit_staff_save', adminView.edit_staff_save, name='edit_staff_save'),
    
    
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
    path('edit_course_save', adminView.edit_course_save, name='edit_course_save'),
    
    # staffs roles
    path('create_schedule', staffView.create_schedule, name='create_schedule'),
    path('add_slots_save', staffView.add_slots_save, name='add_slots_save'),
    
    # students roles
    path('view_lectures', studentView.view_lectures, name='view_lectures'),
    path('add_appointment/<str:staff_id>', studentView.add_appointment, name='add_appointment'),
    path('get_time_slots', studentView.get_time_slots, name='get_time_slots'),
     
     
]