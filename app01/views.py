from django.db.models import Q
from django.shortcuts import render, redirect
from django import views
from django.utils.decorators import method_decorator
from app01.models import User, Classmethod
from app01.toolclass import Tools

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
            request.session.set_expiry(60000)
            return redirect("/classes/")
        else:
            return redirect("/login/")

@method_decorator(outer, name='dispatch')
class Classes(views.View):
    pagename = "班级信息"
    classesmsg = ["班级编号", "班级名称", "操作"]
    count_num = Classmethod.objects.count()
    count = count_num/5
    count_y = count_num%5
    if count_y != 0:
        count += count_y

    def dispatch(self, request, *args, **kwargs):
        ret = super(Classes, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        tool = Tools()
        datalist = tool.list_data(1)
        data = {
            "num": self.count,
            "datalist": datalist,
        }
        return render(request, "classes.html", {"classesmsg": self.classesmsg, "pagename": self.pagename, "data": data})

    def post(self, request, *args, **kwargs):
        pass

class Logout(views.View):
    def get(self, request, *args, **kwargs):
        del request.session["username"]
        return redirect("/login/")

