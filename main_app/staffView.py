from django.shortcuts import render
from .forms import AddTimeSlot

#

def staff_panel(request):
    return render(request,"main_app/staffs/staff_panel.html")

def create_schedule(request):
    form = AddTimeSlot()
    return render(request, "main_app/staffs/staff_schedule.html", {'form':form})