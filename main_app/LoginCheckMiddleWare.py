from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user == "AnonymousUser":
            profile_pic_url = user.profile_pic.url
            if profile_pic_url.startswith(settings.MEDIA_URL):
                return None  
        if user.is_authenticated:
            profile_pic_url=user.profile_pic.url
            if profile_pic_url.startswith(settings.MEDIA_URL):
                return None
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
            if request.path == reverse("login") or request.path == reverse("dblogin") or modulename == "django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("login"))