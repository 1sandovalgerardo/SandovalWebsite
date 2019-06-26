from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib import messages
from .models import List
from .forms import ListForm

# Create your views here.


#class ToDoList(TemplateView):
#    template_name = 'todolist.html'


def ToDoListView(request):
    form = ListForm()
    if request.method == 'POST':
        print('debug1')
        form = ListForm(request.POST)
        if form.is_valid():
            print('debug2')
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to the list!'))
            return render(request, 'todolist.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todolist.html', {'all_items': all_items})