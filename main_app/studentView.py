from django.shortcuts import render

#
def student_panel(request):
    return render(request,"main_app/students/student_panel.html")