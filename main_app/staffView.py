from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddTimeSlot
from .models import TimeSlot, CustomUser, Appointment
from django.contrib import messages
from django.urls import reverse
from datetime import date
from django.core.mail import send_mail
from schoo_demo.settings import EMAIL_HOST_USER

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
    student_email = appointment.student.email
    appointment_details = f'Student Name: {appointment.student.first_name}\nAppointment Time: {appointment.appointment_time}'
    appointment.status=1
    appointment.save()
    send_appointment_accepted_email(student_email, appointment_details)
    return HttpResponseRedirect(reverse('appointments'))

def reject_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = 2
    appointment.save()
    return HttpResponseRedirect(reverse('appointments'))

def staff_profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {'user':user}
    return render(request, 'main_app/staffs/staff_profile.html',context)

def staff_profile_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('staff_profile'))
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
            return HttpResponseRedirect(reverse("staff_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("staff_profile"))

def send_appointment_accepted_email(student_email, appointment_details):
    subject = 'Appointment Accepted'
    message = f'Hi, your appointment has been accepted. Here are the details:\n\n{appointment_details}'
    from_email = EMAIL_HOST_USER
    recipient_list = [student_email]
    send_mail(subject, message, from_email, recipient_list)