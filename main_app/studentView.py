import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Staffs, TimeSlot, Appointment,CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse

#
def student_panel(request):
    return render(request,"main_app/students/student_panel.html")

def view_lectures(request):
    staffs = Staffs.objects.all()
    context = {'staffs':staffs}
    return render(request, 'main_app/students/lectures.html',context)

def add_appointment(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    context = {'staff':staff}
    return render(request,'main_app/students/add_booking.html',context)

@csrf_exempt
def get_time_slots(request):
    staff_id = request.POST.get("staff_id")
    booking_date = request.POST.get("booking_date")
    time_slots = TimeSlot.objects.filter(slot_date=booking_date, staff=staff_id, status=0)
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
        appointment_date = request.POST.get("booking_date")
        appointment_time = request.POST.get("times")
        
        student_obj = CustomUser.objects.get(id = request.user.id)
        
        
        
        try:
            appointment = Appointment.objects.create(
            appointment_date=appointment_date, appointment_time=appointment_time,
            staffId = staff_id,student = student_obj
            )
            appointment.save()
            
            time_slot_status = TimeSlot.objects.get(slot_date=appointment_date)
            time_slot_status.status =1
            time_slot_status.save()
            messages.success(request,"appointment created successfully")
            return HttpResponseRedirect(reverse("add_appointment", kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to make appointment")
            return HttpResponseRedirect(reverse("add_appointment", kwargs={"staff_id":staff_id}))