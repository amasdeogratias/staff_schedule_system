from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .models import *
from django.urls import reverse


#
def admin_home(request):
    return render(request,'main_app/admin/home_content.html')
    
def add_staff(request):
    departments = Department.objects.all()
    return render(request, 'main_app/admin/add_staff.html',{'departments':departments})
    
def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else: # process the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        department_id = request.POST.get('department')  
        
        #create custom user object
        try:
            user = CustomUser.objects.create_user(
               username=username,email=email,password=password,first_name=first_name,last_name=last_name, user_type=2)
            user.staffs.address=address
            depart_obj = Department.objects.get(id=department_id)
            user.staffs.department = depart_obj
            user.save()
            messages.success(request, "Staff added successfully...")
            return HttpResponseRedirect(reverse("add_staff"))
            
        except:
            messages.error(request)
            return HttpResponseRedirect(reverse("add_staff"))
            
def add_department(request):
    return render(request, 'main_app/admin/add_department.html')
    
def add_department_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        department_name = request.POST.get('department_name')
        try:
            department = Department.objects.create(department_name=department_name)
            department.save()
            messages.success(request, 'Department added successfully')
            return HttpResponseRedirect(reverse('add_department'))
        except:
            messages.error(request,'Problem in department creation')
            return HttpResponseRedirect(reverse('add_department'))
            
def all_departments(request):
    departments = Department.objects.all()
    return render(request, 'main_app/admin/view_department.html',{'departments':departments})
    
def add_course(request):
    departments = Department.objects.all()
    return render(request, 'main_app/admin/add_course.html', {'departments':departments})
    
def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        department_id = request.POST.get('department')
        department_obj = Department.objects.get(id=department_id)
        
        try:
            course = Courses.objects.create(course_name=course_name,course_code=course_code,department=department_obj)
            course.save()
            messages.success(request,'Course added successfully')
            return HttpResponseRedirect(reverse('add_course'))
            
        except:
            messages.error(request, 'Problem in course creation')
            return HttpResponseRedirect(reverse('add_course'))
            