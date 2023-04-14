from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user    
        if user.is_authenticated: 
            if user.user_type == "1":
                if modulename == "main_app.adminView":
                    pass
                elif modulename == "main_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_dashboard"))
            elif user.user_type == "2":
                if modulename == "main_app.staffView":
                    pass
                elif modulename == "main_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_panel"))
            elif user.user_type == "3":
                if modulename == "main_app.studentView":
                    pass
                elif modulename == "main_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_panel"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("dblogin"):
                pass
            else:
                return HttpResponseRedirect(reverse("login"))