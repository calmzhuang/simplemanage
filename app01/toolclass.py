from app01.models import User, Classmethod, Student, Teacher

class Tools():
    def class_list_data(self, num):
        a = (int(num)-1)*5
        b = int(num)*5
        return Classmethod.objects.all().values("id", "name").order_by("id")[a:b]

    def student_list_data(self, num):
        a = (int(num) - 1) * 5
        b = int(num) * 5
        return Student.objects.all().values("id", "name", "email", "classes__name").order_by("id")[a:b]

    def teacher_list_data(self, num):
        a = (int(num) - 1) * 5
        b = int(num) * 5
        return Teacher.objects.all().values("id", "name", "email", "classes__name").order_by("id")[a:b]

    def class_list_insert(self, num):
        Classmethod.objects.create(name=num)