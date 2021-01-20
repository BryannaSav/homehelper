from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import CalendarEvent, TaskList, ListItem

@login_required
def dashboard(request):
    task_lists = TaskList.objects.filter(user=request.user.id)
    print(task_lists)
    return render(request, "tasklist/dashboard.html")

def register(request):
    print("Hit reg")
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
    print("hit login")
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

def user_logout(request):
    logout(request)
    return redirect('/')