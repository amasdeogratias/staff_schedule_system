from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from .forms import AddTimeSlot
from .models import TimeSlot, CustomUser, Appointment, Staffs,NotificationStudent,NotificationStaff
from django.contrib import messages
from django.urls import reverse
from datetime import date
from django.core.mail import send_mail
from schoo_demo.settings import EMAIL_HOST_USER
from PIL import Image
from datetime import datetime,date
from django.template.loader import get_template
from xhtml2pdf import pisa



#

def staff_panel(request):
    user = request.user.id
    todayAppointments = Appointment.objects.filter(staffId = user,appointment_date = date.today()).count()
    appointmentcount=Appointment.objects.filter(staffId = request.user.id).count()
    newAppointments = Appointment.objects.filter(status=0).count()
     # count unread notifications
    count_notifications = NotificationStaff.objects.filter(staff=request.user.id,is_read=False).count() #
    notifications = NotificationStaff.objects.filter(staff=request.user.id,is_read=False).order_by('-created_at')
    
    elpsis_message = ''
    for notify in notifications:
        elpsis_message = notify.message[:5] + '...' if len(notify.message) > 5 else notify.message
    notifications.update(is_read=True)
    context = {
            'appointmentcount':appointmentcount,
            'todayAppointments':todayAppointments,
            'newAppointments':newAppointments,
            'count_notifications':count_notifications,
            'notifications':notifications,
            'elpsis_message':elpsis_message,
            }
    return render(request,"main_app/staffs/staff_panel.html", context)

# show unprocessed appointments
def newAppointments(request):
    new_appointments = Appointment.objects.filter(status=0)
    return render(request, 'main_app/staffs/new_appointment.html', {"new_appointments":new_appointments})

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
            undergraduate_time = form.cleaned_data["undergraduate_time"]
            postgraduate_time = form.cleaned_data["postgraduate_time"]
            education_level = form.cleaned_data["education_level"]
            
            if slot_date and undergraduate_time:
                existing_timeslots = TimeSlot.objects.filter(slot_date=slot_date, time=undergraduate_time)
                if existing_timeslots.exists():
                    messages.error(request, 'This timeslot is already taken for the selected date.')
                    return HttpResponseRedirect(reverse('create_schedule'))
                else:
                    try:
                        staff = CustomUser.objects.get(id=request.user.id)
                        if education_level == "undergraduate":
                            timeslot = TimeSlot.objects.create(slot_date = slot_date, time = undergraduate_time, education_level=education_level, staff = staff)
                        elif education_level == "postgraduate":
                            timeslot = TimeSlot.objects.create(slot_date = slot_date, time = postgraduate_time, education_level=education_level, staff = staff)
                        else:
                            messages.error(request, 'No education level selected')
                        timeslot.save()
                        messages.success(request, 'Time slots added successfully')
                        return HttpResponseRedirect(reverse('create_schedule'))
                    except:
                        messages.error(request, 'Problem occurred in creating time slots')
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
    student_email = appointment.student.id  # get student email
    # print(student_email)
    staff_id = appointment.staffId # get lecture id from appoint model
    
    staff_email = CustomUser.objects.get(id=staff_id) # compare id with customuser
    
    student_id = CustomUser.objects.get(id=student_email) # compare id with customuser
    
    from_email = staff_email.email # get lectures email
    
    appointment_details = f'Lecture Name: {appointment.staff_name}, Email: {from_email} \nStudent Name: {appointment.student.first_name}\nAppointment Time: {appointment.appointment_time}'
    appointment.status=1
    appointment.save()
    # send_appointment_accepted_email(student_email, appointment_details)
    NotificationStudent.objects.create(message="Appointment Accepted", student=student_id, is_read=False)
    return HttpResponseRedirect(reverse('appointments'))

def reject_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    student_id = CustomUser.objects.get(id=appointment.student.id) # compare id with customuser
    
    student_email = student_id.email
    appointment_details = f'Lecture Name: {appointment.staff_name}, \nAppointment Reason:{appointment.reason} \nAppointment time:{appointment.appointment_date, appointment.appointment_time}'
    
    appointment.status = 2
    appointment.save()
    NotificationStudent.objects.create(message="Appointment Rejected", student=student_id, is_read=False)
    send_appointment_rejected_email(student_email, appointment_details)
    return HttpResponseRedirect(reverse('appointments'))

def staff_profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {'user':user}
    return render(request, 'main_app/staffs/staff_profile.html',context)

def staff_profile_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('staff_profile'))
    else:
        profile_pic = request.FILES['profile_pic']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password=request.POST.get("password")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic
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
    
def send_appointment_rejected_email(student_email, appointment_details):
    subject = 'Appointment Accepted'
    message = f'Hi, your appointment has been rejected. Here are the details:\n\n{appointment_details}'
    from_email = EMAIL_HOST_USER 
    recipient_list = [student_email]
    send_mail(subject, message, from_email, recipient_list)
    

def view_shedule(request):
    time_slots = TimeSlot.objects.filter(staff=request.user.id).order_by('-created_at')
    context = {
        "time_slots":time_slots
    }
    return render(request, 'main_app/staffs/view_schedule.html', context)

def single_notification(request, notification_id):
    notifys = NotificationStaff.objects.filter(id=notification_id)
    context = {'notifys':notifys}
    return render(request, 'main_app/staffs/single_staff_notification.html', context)

def pdf_appointments(request):
    staff = CustomUser.objects.get(id = request.user.id)
    appointments = Appointment.objects.filter(staffId = request.user.id)
    template_path = 'main_app/staffs/pdf_appointments.html'
    context = {"appointments":appointments, 'staff':staff}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="appointments_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

