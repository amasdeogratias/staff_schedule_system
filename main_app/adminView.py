from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .models import CustomUser, Department, Courses, Staffs, Students
from django.urls import reverse


#
def admin_home(request):
    return render(request,'main_app/admin/home_content.html')

def admin_profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {'user':user}
    return render(request, 'main_app/admin/admin_profile.html', context)

def admin_profile_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('admin_profile'))
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password=request.POST.get("password")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != '':
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
    
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
            
# def all_departments(request):
#     departments = Department.objects.all()
#     return render(request, 'main_app/admin/view_department.html',{'departments':departments})
    
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
            
def add_student(request):
    return render(request, 'main_app/admin/add_student.html')
    
def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else: # process the form
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        program = request.POST.get('program') 
        gender = request.POST.get('gender') 
        session_start = request.POST.get('session_start') 
        session_end = request.POST.get('session_end') 
        
        #create custom user object
        try:
            user = CustomUser.objects.create_user(
               username=username,email=email,password=password,first_name=first_name,last_name=last_name, user_type=3)
            user.students.student_id=student_id
            user.students.program=program
            user.students.gender=gender
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end
            user.save()
            messages.success(request, "Student added successfully...")
            return HttpResponseRedirect(reverse("add_student"))
            
        except:
            messages.error(request,'Failed to add student')
            return HttpResponseRedirect(reverse("add_student"))
            
def view_department(request):
    departments = Department.objects.all()
    context = {'departments':departments}
    return render(request, 'main_app/admin/view_departments.html', context)
    
def view_staff(request):
    staffs = Staffs.objects.all()
    context = {'staffs':staffs}
    return render(request, 'main_app/admin/view_staffs.html', context)
    
def view_student(request):
    students = Students.objects.all()
    context = {'students':students}
    return render(request, 'main_app/admin/view_students.html', context)
            
def view_course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'main_app/admin/view_courses.html', context)

# edit functions    
def edit_department(request,department_id):
    department = Department.objects.get(id=department_id)
    context = {'department':department, 'id':department_id}
    return render(request, 'main_app/admin/edit_department.html', context)
    
def edit_department_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name')
        
        try:
            department = Department.objects.get(id=department_id)
            department.department_name=department_name
            department.save()
            messages.success(request, 'Department updated successfully')
            return HttpResponseRedirect(reverse('edit_department', kwargs={'department_id':department_id}))
        except:
            messages.error(request,'Failed to update department')
            return HttpResponseRedirect(reverse('edit_department', kwargs={'department_id':department_id}))
            
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    departments = Department.objects.all()
    context = {'course':course, 'departments':departments, 'id':course_id}
    return render(request, 'main_app/admin/edit_course.html', context)
    
def edit_course_save(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        course_id = request.POST.get('course_id')
        department_id = request.POST.get('department')
        
        
        try:
            course = Courses.objects.get(id=course_id)
            department_obj = Department.objects.get(id=department_id)
            course.course_name = course_name
            course.course_code = course_code
            course.department = department_obj
            course.save()
            messages.success(request,'Course updated successfully')
            return HttpResponseRedirect(reverse('edit_course', kwargs={'course_id':course_id}))
            
        except:
            messages.error(request, 'Failed to update course')
            return HttpResponseRedirect(reverse('edit_course',kwargs={'course_id':course_id}))
        
def edit_staff(request, staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    departments = Department.objects.all()
    context = {'staff':staff,'departments':departments}
    return render(request,'main_app/admin/edit_staff.html', context)

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request,"Staff updated successfully")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        
def edit_student(request, stud_id):
    student=Students.objects.get(admin=stud_id)
    context = {'student':student}
    return render(request,'main_app/admin/edit_student.html', context)

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        stud_id=request.POST.get("stud_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        program=request.POST.get("program")
        gender=request.POST.get("gender")

        try:
            user=CustomUser.objects.get(id=stud_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            student_model=Students.objects.get(admin=stud_id)
            student_model.program=program
            student_model.gender=gender
            student_model.save()
            messages.success(request,"Student updated successfully")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"stud_id":stud_id}))
        except:
            messages.error(request,"Failed to Edit Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"stud_id":stud_id}))
