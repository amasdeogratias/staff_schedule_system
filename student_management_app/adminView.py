from django.shortcuts import render


#
def admin_home(request):
    return render(request,'student_management_app/admin/main_content.html')