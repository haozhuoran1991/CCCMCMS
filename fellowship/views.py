from django.shortcuts import render
from django.http import HttpResponse
from fellowship.models import fellowship
# Create your views here.


def fellowship_detail(request):
    Fellowship = fellowship.objects.all()
    return render(request, 'fellowship.html',{'Fellowship':Fellowship})