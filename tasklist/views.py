from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from itertools import chain

from .forms import RegisterForm
from .models import CalendarEvent, TaskList, ListItem
from datetime import timedelta, date
import json

def sort_helper(queryset):
    try:
        return queryset.start_date
    except:
        return queryset.due_date

@login_required
def dashboard(request):
    start_day = date.today()
    end_date = start_day.today() + timedelta(days=7)
    upcoming_events = CalendarEvent.objects.filter(user=request.user.id, 
        start_date__range=[start_day, end_date]).order_by('start_date')
    upcoming_tasks = ListItem.objects.filter(user=request.user.id, 
        due_date__range=[start_day, end_date], completed=False).order_by('due_date')
    all_upcoming = list(chain(upcoming_events, upcoming_tasks))
    all_upcoming = sorted(all_upcoming, key = sort_helper)
    return render(request, 'tasklist/dashboard.html', 
        {'all_upcoming' : all_upcoming})

def register(request):
    if request.method == 'POST':
        print('POST')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/dashboard')
    else:
        form = RegisterForm()
    return render(request, 'tasklist/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print('proper login')
                return redirect('/dashboard')
            else:
                print('User in none')
        else:
            print('Not valid form')
    form = AuthenticationForm()
    return render(request, 'tasklist/login.html', {'form':form})

@login_required
def lists(request):
    lists = TaskList.objects.filter(user=request.user.id)
    return render(request, 'tasklist/lists.html', {'lists': lists})


@login_required
def create_list(request):
    if request.method == 'POST':
        task_list = TaskList(name=request.POST['name'], 
            description=request.POST['description'], 
            user=request.user)
        task_list.save()
    return redirect("/lists")

@login_required
def create_task(request, id):
    if request.method == 'POST':
        task_list = TaskList.objects.get(id=id)
        list_item = ListItem(task=request.POST['task'], 
            due_date=request.POST['due_date'], 
            task_list=task_list,
            user=request.user)
        list_item.save()
        # task_list.save()
    return redirect("/list/"+str(id))

@login_required
def one_list(request, id):
    task_list = TaskList.objects.get(id=id)
    list_items = ListItem.objects.filter(task_list=id)
    return render(request, 'tasklist/one_list.html', 
        {'task_list': task_list, 'list_items': list_items})

def user_logout(request):
    logout(request)
    return redirect('/')

def api_one_day(request, date):
    year, month, day = date.split('-')
    day_events = CalendarEvent.objects.filter(start_date__year=year, 
        start_date__month=month,start_date__day=day).values()
    day_tasks = ListItem.objects.filter(due_date__year=year, 
        due_date__month=month,due_date__day=day).values()
    day_items = list(chain(day_events, day_tasks))
    return JsonResponse({'day_items': day_items})

def api_complete_task(request, id):
    task = ListItem.objects.get(id=id)
    print("Before: " + str(task.completed))
    task.completed = not task.completed
    print("After: " + str(task.completed))
    task.save()
    return JsonResponse({'status': 'complete'})

def testroute(request):
    return JsonResponse({"STUFF": "SUCCESS"})