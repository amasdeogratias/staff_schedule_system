from django.shortcuts import render

# Create your views here.
def showDemoPage(request):
    return render(request, 'student_management_app/demo.html')
    
def showLoginPage(request):
    return render(request, 'student_management_app/login.html')
