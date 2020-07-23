from django.shortcuts import render
import datetime


def home(request):
    date = datetime.date.today()
    return render(request, 'home/home.html',{"date": date})

def realestate(request):
    date = datetime.date.today()
    return render(request, 'home/realestate.html',{"date": date})
