from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .EmailBackEnd import EmailBackEnd
from django.contrib import messages


# Create your views here.
def showDemoPage(request):
    return render(request, 'student_management_app/demo.html')
 
def home(request):
    return render(request, 'student_management_app/welcome.html')   
    
def showLoginPage(request):
    return render(request, 'student_management_app/login.html')
    
def dbLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request,user)
            return HttpResponse("Email :"+request.POST.get('email')+" Password: "+request.POST.get('password'))
        else:
            messages.error(request,'Invalid email or password')
            return HttpResponseRedirect("login")
            
def getUserDetails(request):
    if request.user != None:
        return HttpResponse("User : "+request.user.email+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse('Please login first')
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
