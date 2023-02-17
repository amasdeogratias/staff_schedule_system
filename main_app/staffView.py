from django.shortcuts import render

#
def staff_panel(request):
    return render(request,"main_app/staffs/staff_panel.html")

def create_schedule(request):
    return render(request, "main_app/staffs/staff_schedule.html")