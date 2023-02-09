from django.shortcuts import render


#
def admin_home(request):
    return render(request,'main_app/admin/home_content.html')
    
def add_staff(request):
    return render(request, 'main_app/admin/add_staff.html')