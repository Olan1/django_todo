from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ToDoItem

def index(request):
    todos = ToDoItem.objects.all().values()
    template = loader.get_template('todolist.html')
    context = {
        'todos': todos,
    }
    return HttpResponse(template.render(context, request))