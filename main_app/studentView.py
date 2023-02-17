from django.shortcuts import render

#
def student_panel(request):
    return render(request,"main_app/students/student_panel.html")

def view_lectures(request):
    return render(request, 'main_app/students/lectures.html')

def add_appointment(request):
    return render(request,'main_app/students/add_booking.html')