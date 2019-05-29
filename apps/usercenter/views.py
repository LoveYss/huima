from django.shortcuts import render
from django.views import View
from usercenter.models import User


# Create your views here.
class UserCenter(View):
    def get(self, request, uid):
        user = User.objects.get(id=uid)
        return render(request, 'usercenter/usercenter.html', locals())
