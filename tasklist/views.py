from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import timedelta, date

from .forms import RegisterForm
from .models import (
    CalendarEvent, TaskList, ListItem, 
    TaskListForm, ListItemForm, CalendarEventForm
)

# Allows multiple querysets to be sorted by dates with different field names 
def sort_helper(queryset):
    try:
        return queryset.start_date
    except:
        return queryset.due_date

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/dashboard')
    else:
        form = RegisterForm()
    return render(request, 'tasklist/register.html', {'form':form})

def user_login(request):
    error = None
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
        error = 'Invalid login'
    form = AuthenticationForm()
    return render(request, 'tasklist/login.html', {'form':form, 'error':error})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    start_day = date.today()
    end_date = start_day.today() + timedelta(days=7)
    upcoming_events = (
        CalendarEvent
        .objects
        .filter(user=request.user.id, start_date__range=[start_day, end_date])
        .order_by('start_date')
    )
    upcoming_tasks = (
        ListItem
        .objects
        .filter(user=request.user.id, completed=False, 
                due_date__range=[start_day, end_date])
        .order_by('due_date')
    )
    all_upcoming = list(upcoming_events) + list(upcoming_tasks)
    all_upcoming = sorted(all_upcoming, key = sort_helper)
    return render(request, 'tasklist/dashboard.html', 
                 {'all_upcoming' : all_upcoming})

@login_required
def lists(request):
    lists = TaskList.objects.filter(user=request.user.id)
    return render(request, 'tasklist/lists.html', {'lists': lists})

@login_required
def create_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            task_list = TaskList(
                            name=request.POST['name'], 
                            description=request.POST['description'], 
                            user=request.user)
            task_list.save()
    return redirect('/lists')

@login_required
def one_list(request, id):
    task_list = TaskList.objects.get(id=id)
    list_items = (
        ListItem
        .objects
        .filter(task_list=id)
        .order_by('completed', 'due_date')
    )
    return render(request, 'tasklist/one_list.html', 
                 {'task_list': task_list, 'list_items': list_items})

@login_required
def edit_list(request, id):
    if request.method == 'POST':
        task_list = TaskList.objects.get(id=id)
        task_list.name = request.POST['name'] 
        task_list.description = request.POST['description']
        task_list.save()
    return redirect('/lists')

@login_required
def delete_list(request, id):
    task_list = TaskList.objects.get(id=id)
    task_list.delete()
    return redirect('/lists')

@login_required
def create_task(request, id):
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            task_list = TaskList.objects.get(id=id)
            list_item = ListItem(
                            task=request.POST['task'], 
                            due_date=request.POST['due_date'], 
                            task_list=task_list,
                            user=request.user)
            list_item.save()
    return redirect('/list/' + str(id))

@login_required
def edit_task(request, item_id, list_id):
    if request.method == 'POST':
        list_item = ListItem.objects.get(id=item_id)
        list_item.task = request.POST['task'] 
        list_item.due_date = request.POST['due_date']
        list_item.save()
    return redirect('/list/' + str(list_id))

@login_required
def delete_task(request, item_id, list_id):
    list_item = ListItem.objects.get(id=item_id)
    list_item.delete()
    return redirect('/list/' + str(list_id))

@login_required
def calendar(request):
    return render(request, 'tasklist/calendar.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            calendar_event = CalendarEvent(
                                name=request.POST['name'], 
                                start_date=request.POST['start_date'], 
                                user=request.user)
            calendar_event.save()
    return redirect('/calendar')

def api_calendar(request):
    calendar_events = list(
        CalendarEvent
        .objects
        .filter(user=request.user.id)
        .values()
    )
    for calendar_event in calendar_events:
        start_date = calendar_event['start_date']
        calendar_event['start'] = start_date.strftime('%Y-%m-%d %H:%M')
        calendar_event.pop('start_date')
    return JsonResponse({'calendar_events': calendar_events})

def api_one_day(request, date):
    # Formatting start_date & due_date so vue can display on calendar
    year, month, day = date.split('-')
    day_events = (
        CalendarEvent
        .objects
        .filter(start_date__year=year, start_date__month=month, 
                start_date__day=day)
        .values()
    )
    day_tasks = (
        ListItem
        .objects
        .filter(due_date__year=year, due_date__month=month, 
                due_date__day=day)
        .values()
    )
    day_items = list(day_events) + list(day_tasks)
    return JsonResponse({'day_items': day_items})

def api_complete_task(request, id):
    #toggles complete status
    task = ListItem.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'status': 'complete'})
