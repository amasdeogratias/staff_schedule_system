import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Staffs, TimeSlot
from django.views.decorators.csrf import csrf_exempt

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
    time_slots = TimeSlot.objects.filter(slot_date=booking_date, staff=staff_id)
    list_data = []
    
    for slot in time_slots:
        data_small = {"time":slot.time} # add data in dictionary
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)