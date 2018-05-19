from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from django import views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict
from app01.models import User, Classmethod, Student, Teacher
from app01.toolclass import Tools
import json, random

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
    count = count_num//5
    count_y = count_num%5
    if count_y != 0:
        count += 1

    def dispatch(self, request, *args, **kwargs):
        ret = super(Classes, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        tool = Tools()
        datalist = tool.class_list_data(1)
        data = {
            "num": self.count,
            "datalist": datalist,
        }
        return render(request, "classes.html", {"classesmsg": self.classesmsg, "pagename": self.pagename, "data": data})

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        tool = Tools()
        num = request.POST.get("num")
        datalist = list(tool.class_list_data(num))
        print(datalist)
        # datalist = model_to_dict(data_list)
        # print(datalist)
        # datalist = serializers.serialize('json', datalist)
        data = {
            "classesmsg": self.classesmsg,
            "datalist": datalist,
        }
        data = json.dumps(data)
        print(data)
        return HttpResponse(data)

@method_decorator(outer, name='dispatch')
class Students(views.View):
    pagename = "学生信息"
    classesmsg = ["学生编号", "学生名称", "学生邮箱", "所在班级", "操作"]
    count_num = Student.objects.count()
    count = count_num//5
    count_y = count_num%5
    if count_y != 0:
        count += 1

    def dispatch(self, request, *args, **kwargs):
        ret = super(Students, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        tool = Tools()
        datalist = tool.student_list_data(1)
        print(datalist)
        data = {
            "num": self.count,
            "datalist": datalist,
        }
        return render(request, "student.html", {"classesmsg": self.classesmsg, "pagename": self.pagename, "data": data})

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        tool = Tools()
        num = request.POST.get("num")
        datalist = list(tool.student_list_data(num))
        print(datalist)
        # datalist = model_to_dict(data_list)
        # print(datalist)
        # datalist = serializers.serialize('json', datalist)
        data = {
            "classesmsg": self.classesmsg,
            "datalist": datalist,
        }
        data = json.dumps(data)
        print(data)
        return HttpResponse(data)

@method_decorator(outer, name='dispatch')
class Teachers(views.View):
    pagename = "教师信息"
    classesmsg = ["教师编号", "教师姓名", "教师邮箱", "所在班级", "操作"]
    count_num = Teacher.objects.count()
    count = count_num//5
    count_y = count_num%5
    if count_y != 0:
        count += 1

    def dispatch(self, request, *args, **kwargs):
        ret = super(Teachers, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        tool = Tools()
        datalist = tool.teacher_list_data(1)
        data = {
            "num": self.count,
            "datalist": datalist,
        }
        return render(request, "teacher.html", {"classesmsg": self.classesmsg, "pagename": self.pagename, "data": data})

    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        tool = Tools()
        num = request.POST.get("num")
        datalist = list(tool.teacher_list_data(num))
        # datalist = model_to_dict(data_list)
        # print(datalist)
        # datalist = serializers.serialize('json', datalist)
        data = {
            "classesmsg": self.classesmsg,
            "datalist": datalist,
        }
        data = json.dumps(data)
        return HttpResponse(data)

class Logout(views.View):
    def get(self, request, *args, **kwargs):
        del request.session["username"]
        return redirect("/login/")

