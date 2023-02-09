from django.shortcuts import render


#
def admin_home(request):
    return render(request,'main_app/admin/home_content.html')