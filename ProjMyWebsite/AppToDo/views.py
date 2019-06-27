from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def ToDoListView(request):
    if request.method == "POST":
        form = ListForm(request.POST)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item Added'))
            return render(request, 'todolist.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todolist.html', {'all_items': all_items})

def Delete(request, pk):
    item = List.objects.get(pk=pk)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return render(request, 'todolist.html')

