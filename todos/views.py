from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import ToDoItem


def index(request):
    todos = ToDoItem.objects.all().values()
    template = loader.get_template('todolist.html')
    context = {
        'todos': todos,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    item = request.POST['item']
    urgent = request.POST.get('urgent') == 'on'
    todo = ToDoItem(item=item, urgent=urgent)
    todo.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    todo = ToDoItem.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))


def edit(request, id):
    todo = ToDoItem.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
        'todo': todo
    }
    return HttpResponse(template.render(context, request))


def editrecord(request, id):
    item = request.POST['item']
    urgent = request.POST.get('urgent') == 'on'
    todo = ToDoItem.objects.get(id=id)
    todo.item = item
    todo.urgent = urgent
    todo.save()
    return HttpResponseRedirect(reverse('index'))
