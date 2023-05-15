import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Staffs, TimeSlot, Appointment,CustomUser, Students, NotificationStudent,NotificationStaff
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from datetime import date

#
def student_panel(request):
    appointments = Appointment.objects.all()
    context = {'appointments':appointments}
    return render(request,"main_app/students/student_panel.html",context)

def view_lectures(request):
    staffs = Staffs.objects.all()
    context = {'staffs':staffs}
    return render(request, 'main_app/students/lectures.html',context)

def add_appointment(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    todayDate = date.today().strftime('%Y-%m-%d')
    context = {'staff':staff, "todayDate":todayDate}
    return render(request,'main_app/students/add_booking.html',context)

@csrf_exempt
def get_time_slots(request):
    staff_id = request.POST.get("staff_id")
    booking_date = request.POST.get("booking_date")
    
    # get student current login
    student_login = CustomUser.objects.get(id=request.user.id)
    student_id = Students.objects.get(admin = student_login)
    
    # filter time slots by education level
    if student_id.level == "Undergraduate":
        time_slots = TimeSlot.objects.filter(slot_date=booking_date, staff=staff_id, status=0, education_level='undergraduate')
        list_data = []
        
        for slot in time_slots:
            data_small = {"time":slot.time} # add data in dictionary
            list_data.append(data_small)
        return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
    else:
        time_slots = TimeSlot.objects.filter(slot_date=booking_date, staff=staff_id, status=0, education_level='postgraduate')
        list_data = []
        
        for slot in time_slots:
            data_small = {"time":slot.time} # add data in dictionary
            list_data.append(data_small)
        return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

def add_booking_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not Allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        appointment_reason = request.POST.get("reason").upper()
        appointment_date = request.POST.get("booking_date")
        appointment_time = request.POST.get("times")
        
        student_obj = CustomUser.objects.get(id = request.user.id)

        staff = Staffs.objects.get(admin = staff_id)
        # return HttpResponse(staff.admin.first_name + ' ' + staff.admin.last_name)
        
        
        
        try:
            appointment = Appointment.objects.create(
            reason= appointment_reason, appointment_date=appointment_date, appointment_time=appointment_time,
            staffId = staff_id, 
            staff_name=staff.admin.first_name + ' ' +staff.admin.last_name, 
            student = student_obj,status=0
            )
            appointment.save()
            
            time_slot_status = TimeSlot.objects.get(slot_date=appointment_date,time=appointment_time)
            time_slot_status.status = 1
            time_slot_status.save()
            NotificationStaff.objects.create(message="Appointment Accepted", staff=staff_id, is_read=False)
            messages.success(request,"appointment created successfully")
            return HttpResponseRedirect(reverse("add_appointment", kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to make appointment")
            return HttpResponseRedirect(reverse("add_appointment", kwargs={"staff_id":staff_id}))
        
def student_profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {'user':user}
    return render(request, 'main_app/students/student_profile.html',context)

def student_profile_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('student_profile'))
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
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        
        
def notifications(request):
    user = request.user.id
    # count unread notifications
    count_notifications = NotificationStudent.objects.filter(student=user,is_read=False).count()
    notifications = NotificationStudent.objects.filter(student=user).order_by('-created_at')
    # notifications.update(is_read=True)
    notify = {
        'notifications': notifications, 
        'count_notifications':count_notifications
        }
    return render(request, 'main_app/students/notification.html', context=notify)