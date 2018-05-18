from django.db import models

# Create your models here.
class Classmethod(models.Model):
    name = models.CharField('教室名称', max_length=64)

class Student(models.Model):
    name = models.CharField('学生姓名', max_length=64)
    email = models.CharField('学生邮箱', max_length=64)
    classes = models.ForeignKey('Classmethod',on_delete=models.CASCADE)

class Teacher(models.Model):
    name = models.CharField('教师姓名', max_length=64)
    email = models.CharField('教师邮箱', max_length=64)
    classes = models.ManyToManyField('Classmethod')

class User(models.Model):
    name = models.CharField('用户姓名', max_length=64)
    pwd = models.CharField('用户密码', max_length=64)
