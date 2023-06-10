from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.contrib.auth.views import resolve_url


class LoginCheckMiddleWare(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "main_app.adminView" or modulename == "django.views.static":
                    pass
                elif modulename == "main_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_dashboard"))
            elif user.user_type == "2":
                if modulename == "main_app.staffView" or modulename == "django.views.static":
                    pass
                elif modulename == "main_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_panel"))
            elif user.user_type == "3":
                if modulename == "main_app.studentView" or modulename == "django.views.static":
                    pass
                elif modulename == "main_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_panel"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("dblogin") or modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("login"))
        
        # if user.is_authenticated and hasattr(user, 'profile_pic') and not user.profile_pic:
        #     # Handle the case when user doesn't have a profile picture
        #     # For example, redirect them to a default profile picture or display a placeholder image
        #     pass

        # return None