from django.shortcuts import render, redirect, get_object_or_404
from .models import Mytodo
from .forms import Todoform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    if request.user.is_authenticated:
        tasks = Mytodo.objects.filter(user=request.user)
    else:
        tasks = Mytodo.objects.none()
    form = Todoform()
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')
    return render(request, 'home.html', {'tasks': tasks, 'form': form})

@login_required
def deleteitems(request, edit):
    item = get_object_or_404(Mytodo, id=edit, user=request.user)
    item.delete()
    return redirect('home')

@login_required
def edititems(request, edit):
    item = get_object_or_404(Mytodo, id=edit, user=request.user)
    updateform = Todoform(instance=item)
    if request.method == 'POST':
        updateform = Todoform(request.POST, instance=item)
        if updateform.is_valid():
            updateform.save()
            return redirect('home')
    return render(request, 'update.html', {'updateform': updateform, 'item': item})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Username or Password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                error_message = 'Username already exists'
                return render(request, 'register.html', {'error_message': error_message})
            else:
                try:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    auth.login(request, user)
                    return redirect('login')
                except Exception as e:
                    error_message = f'Error creating account: {e}'
                    return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = "Passwords don't match"
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
