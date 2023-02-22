from django.shortcuts import render
from .models import Staffs

#
def student_panel(request):
    return render(request,"main_app/students/student_panel.html")

def view_lectures(request):
    staffs = Staffs.objects.all()
    context = {'staffs':staffs}
    return render(request, 'main_app/students/lectures.html',context)

def add_appointment(request):
    return render(request,'main_app/students/add_booking.html')