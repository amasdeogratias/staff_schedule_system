from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .models import *
from django.urls import reverse


#
def admin_home(request):
    return render(request,'main_app/admin/home_content.html')
    
def add_staff(request):
    return render(request, 'main_app/admin/add_staff.html')
    
def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else: # process the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        
        #create custom user object
        try:
            user = CustomUser.objects.create_user(
               username=username,email=email,password=password,first_name=first_name,last_name=last_name, user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request, "Staff added successfully...")
            return HttpResponseRedirect(reverse("add_staff"))
            
        except:
            messages.error(request, "Problem in Staff creation...")
            return HttpResponseRedirect(reverse("add_staff"))
            
def add_department(request):
    return render(request, 'main_app/admin/add_department.html')
            