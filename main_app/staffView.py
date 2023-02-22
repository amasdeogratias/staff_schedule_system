from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import AddTimeSlot
from .models import TimeSlot, CustomUser
from django.contrib import messages
from django.urls import reverse

#

def staff_panel(request):
    return render(request,"main_app/staffs/staff_panel.html")

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
