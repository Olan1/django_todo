from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    # Gets all objects of class Item
    items = Item.objects.all()
    # Place class objects into dictionary
    context = {
        'items': items
    }
    # Pass class objects dictionary as arguement
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # If request method is a POST request:
    if request.method == 'POST':
        # Post the form to the DB
        form = ItemForm(request.POST)
        # Check if the form fields are validated against the DB
        if form.is_valid():
            # Save the form data to the DB and render homepage
            form.save()
            return redirect('get_todo_list')
    # If request method is a GET request
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
    
    
def edit_item(request, item_id):
    # Get instance of the Item model in DB if it exists using item_id
    item = get_object_or_404(Item, id=item_id)
    # instance=item prefills form with item data
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    if request.method == 'POST':
        # Post the form to the DB with instance to be updated
        form = ItemForm(request.POST, instance=item)
        # Check if the form fields are validated against the DB
        if form.is_valid():
            # Save the form data to the DB and render homepage
            form.save()
            return redirect('get_todo_list')
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')
    
    
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
