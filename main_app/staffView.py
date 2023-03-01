from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddTimeSlot
from .models import TimeSlot, CustomUser, Appointment
from django.contrib import messages
from django.urls import reverse
from datetime import date

#

def staff_panel(request):
    todayAppointments = Appointment.objects.filter(staffId = request.user.id,appointment_date = date.today()).count()
    appointmentcount=Appointment.objects.filter(staffId = request.user.id).count()
    context = {
            'appointmentcount':appointmentcount,
            'todayAppointments':todayAppointments
            }
    return render(request,"main_app/staffs/staff_panel.html", context)

def create_schedule(request):
    form = AddTimeSlot()
    return render(request, "main_app/staffs/staff_schedule.html", {'form':form})
    
def add_slots_save(request):
    if request.method != "POST":
        return HttpResponse('<h2>Method not Allowed</h2>')
    else:
        form = AddTimeSlot(request.POST)
        if form.is_valid():
            slot_date = form.cleaned_data["slot_date"]
            slot_time = form.cleaned_data["time"]
            
            try:
                staff = CustomUser.objects.get(id=request.user.id)
                timeslot = TimeSlot.objects.create(slot_date = slot_date, time = slot_time, staff = staff)
                timeslot.save()
                messages.success(request, 'Time slots added successfully')
                return HttpResponseRedirect(reverse('create_schedule'))
            except:
                messages.error(request, 'Problem occuered in creating time slots')
                return HttpResponseRedirect(reverse('create_schedule'))
        else:
            form=AddTimeSlot(request.POST)
            return render(request, "main_app/staffs/staff_schedule.html", {"form": form})

def view_appointments(request):
    staff = CustomUser.objects.get(id = request.user.id)
    appointments = Appointment.objects.filter(staffId = request.user.id)
    context = {"appointments":appointments, 'staff':staff}
    return render(request, 'main_app/staffs/all_booking.html', context)

def approve_appointment(request,appointment_id):
    appointment=Appointment.objects.get(id=appointment_id)
    appointment.status=True
    appointment.save()
    return HttpResponseRedirect(reverse('appointments'))