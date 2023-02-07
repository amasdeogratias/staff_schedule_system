from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def showDemoPage(request):
    return render(request, 'student_management_app/demo.html')
    
def showLoginPage(request):
    return render(request, 'student_management_app/login.html')
    
def dbLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        return HttpResponse("Email :"+request.POST.get('email')+"Password: "+request.POST.get('password'))
