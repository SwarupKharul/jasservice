from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime

from .Forms import CustomerForm
from .models import Customer
from django.utils import timezone

date = datetime.date.today()

def portal(request):
    return render(request, 'customer/customerportal.html',{"date": date})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'customer/signupuser.html', {'form': UserCreationForm(),"date": date})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                email = request.POST['email'].lower()
                r = User.objects.filter(email=email)
                if r.count()==0:
                    return render(request, 'customer/signupuser.html',
                                  {'error': 'Email already exists',"date": date})
                else:
                    user.save()
                    login(request, user)
                    return redirect('customer:info')

            except IntegrityError:
                return render(request, 'customer/signupuser.html',
                              {'error': 'This username has already been taken. Please choose a new Username'})
            except ValueError:
                return render(request, 'customer/signupuser.html',
                              {'error': 'Please enter valid username',"date": date})
        else:
            # tell the user the password didn't match
            return render(request, 'customer/signupuser.html', {'error': 'Passwords did not match'})

