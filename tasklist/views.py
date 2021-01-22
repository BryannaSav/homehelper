from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import CalendarEvent, TaskList, ListItem
from datetime import timedelta, date
import json


@login_required
def dashboard(request):
    start_day = date.today()
    end_date = start_day.today() + timedelta(days=7)
    upcoming_events = CalendarEvent.objects.filter(user=request.user.id, 
        start_date__range=[start_day, end_date]).order_by('start_date')
    upcoming_tasks = ListItem.objects.filter(user=request.user.id, 
        due_date__range=[start_day, end_date]).order_by('due_date')
    return render(request, "tasklist/dashboard.html", {'upcoming_events':upcoming_events, 'upcoming_tasks':upcoming_tasks})

def register(request):
    if request.method == "POST":
        print("POST")
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/dashboard")
    else:
        form = RegisterForm()
    return render(request, "tasklist/register.html", {"form":form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("proper login")
                return redirect('/dashboard')
            else:
                print("User in none")
        else:
            print("Not valid form")
    form = AuthenticationForm()
    return render(request, "tasklist/login.html", {"form":form})

# def lists(request):
#     lists = TaskList.objects.filter(user=request.user.id)
#     return render(request, "tasklist/lists.html", {lists: lists})

def user_logout(request):
    logout(request)
    return redirect('/')


def testroute(request):
    context = {
        'cat': json.dumps({
            'name':'Sam',
            'age' : '8 months',
            'status' : 'cute'
        })
    }
    return render(request, 'tasklist/index.html', context)