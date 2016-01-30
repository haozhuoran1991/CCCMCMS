from django.shortcuts import render
from django.http import HttpResponse
from .models import daily_motto
from .models import SundaySchool
# Create your views here.


def index(request):
    Motto = daily_motto.objects.all()[0]
    SunSchool = SundaySchool.objects.all()[:4]
    print(Motto)
    return render(request, 'base.html',{'Motto':Motto, 'SunSchool':SunSchool})


def contact(request):
    return render(request,'contact.html')