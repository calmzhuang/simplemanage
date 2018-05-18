from app01.models import User, Classmethod

class Tools():
    def list_data(self, num):
        a = (num-1)*5
        b = num*5
        return Classmethod.objects.all()[a:b]