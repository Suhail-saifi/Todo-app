from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def home(request):
    tasks = Mytodo.objects.all()
    form = Todoform()
    if request.method == 'POST':
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home.html', {'tasks' : tasks, 'form': form})

def deleteitems(request, edit):
    item = Mytodo.objects.get(id=edit)
    item.delete()
    return redirect('home')

def edititems(request, edit):
    item = get_object_or_404(Mytodo, id=edit)
    updateform = Todoform(instance=item)
    if request.method == 'POST':
        updateform = Todoform(request.POST, instance=item)
        if updateform.is_valid():
            updateform.save()
            return redirect('home')
    return render(request, 'update.html', {'updateform': updateform, 'item': item})