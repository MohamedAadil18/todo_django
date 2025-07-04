from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from .models import TodoTasks

def index(request):
    form = LoginForm()
    if request.user.is_authenticated:
        tasks = TodoTasks.objects.filter(user=request.user)
        return render(request, 'todo.html', {'form' : form, 'tasks': tasks})
    else:
        return render(request, 'todo.html', {'form' : form})

def home_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Enter a valid credentials')
        return render(request, 'todo.html', {'form' : form})

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('home')
    return render(request, 'signup.html', {'form' : form})

def logout_page(request):
    logout(request)
    return redirect('home')

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.get('todo')
        TodoTasks.objects.create(user = request.user, task = task)
        return redirect('home')

def remove_task(request, id):
    if request.method == 'POST':
        get_object_or_404(TodoTasks, id=id).delete()
        return redirect('home')
    return redirect('home')

def update_task(request, id):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        todo = get_object_or_404(TodoTasks, id=id)
        tasks = TodoTasks.objects.filter(user=request.user)
        return render(request, 'todo.html', {'form' : form,
            'tasks': tasks,
            'todo':todo,
            'update':True,
        })
def update_todo(request, id):
    if request.method == 'POST':
        task = request.POST.get('task')
        todo = get_object_or_404(TodoTasks, id=id)
        todo.task = task
        todo.save()
        return redirect('home')