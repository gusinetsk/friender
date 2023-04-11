from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Users,Establishments
import datetime


def main_page(request):
    return render(request,'main.html')


def all_friends(request):
    context = {
        'friends': Users.objects.all(),
    }
    return render(request,'friends.html',context = context)

def all_establishment(request):
    context = {
        'establishments': Establishments.objects.all()
    }
    return render(request,'establishments.html',context = context)




