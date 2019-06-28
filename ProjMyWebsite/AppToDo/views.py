from django.shortcuts import render, redirect
from AppToDo.models import List
from AppToDo.forms import ListForm
from django.contrib import messages


def ToDoListView(request):
    form = ListForm()# this line might not be needed.
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Added'))
            return render(request, 'todolist.html', {'all_items': all_items})
        else:
             messages.error(request, "Please enter a task")
             return redirect('/todolist')
    else:
        all_items = List.objects.all
        return render(request, 'todolist.html', {'all_items': all_items})


def Edit(request, pk):
    if request.method == 'POST':
        item = List.objects.get(pk=pk)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been changed'))
            return redirect('/todolist')
    else:
        item = List.objects.get(pk=pk)
        return render(request, 'edit.html', {'item': item})


def Delete(request, pk):
    if 'Cancel' in request.POST:
        return redirect('/todolist')
    else:
        item = List.objects.get(pk=pk)
        item.delete()
        messages.success(request, ('Item has been deleted'))
        return redirect('/todolist')


def cross_off(request, pk):
    item = List.objects.get(pk=pk)
    item.completed = True
    item.save()
    return redirect('/todolist')


def uncross(request, pk):
    item = List.objects.get(pk=pk)
    item.completed = False
    item.save()
    return redirect('/todolist')

