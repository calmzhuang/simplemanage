from django.db.models import Q
from django.shortcuts import render, redirect
from django import views
from django.utils.decorators import method_decorator
from app01.models import User

# Create your views here.

def outer(func):
    def inner(request, *args, **kwargs):
        sess = request.session.get('username', None)
        if sess:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login')
    return inner

# @method_decorator(outer, name='dispatch')
class Login(views.View):
    def dispatch(self, request, *args, **kwargs):
        # print(111)
        ret = super(Login, self).dispatch(request, *args, **kwargs)
        # print(222)
        return ret

    # @method_decorator(outer)
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(Q(name=username) & Q(pwd=password)).first()
        if user:
            request.session["username"] = user.name
            request.session.set_expiry(600)
            return redirect("/classes/")
        else:
            return redirect("/login/")

@method_decorator(outer, name='get')
class Classes(views.View):
    def get(self, request, *args, **kwargs):
        pagename = "班级信息"
        classesmsg = ["班级编号", "班级名称", "操作"]
        return render(request, "classes.html", {"classesmsg": classesmsg, "pagename": pagename})

class Logout(views.View):
    def get(self, request, *args, **kwargs):
        del request.session["username"]
        return redirect("/login/")


