from django.shortcuts import render
import datetime
from .models import Deals
from django.core.mail import send_mail

date = datetime.date.today()

def home(request):
    deals = Deals.objects.all()
    n=0
    for deal in deals:
       n=n+1
    return render(request, 'home/home.html',{"date": date, 'deals':deals,'n':n})

def insurance(request):
    return render(request, 'home/insurance.html',{"date": date})

def property(request):
    return render(request, 'home/property.html',{"date": date})

def loan(request):
    return render(request, 'home/loan.html',{"date": date})

def aboutus(request):
    return render(request, 'home/aboutus.html',{"date": date})

def career(request):
    return render(request, 'home/career.html',{"date": date})

def suggestion(request):
    return render(request, 'home/suggestion.html',{"date": date})

def sendemail(request):
    send_mail('Hello this is trial','This automated message','sk2todos@gmail.com',['kharulswarupsk@gmail.com'], fail_silently=False)
    return render(request, 'home/sendemail.html',{"date": date})

