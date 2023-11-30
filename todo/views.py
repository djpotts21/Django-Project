<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
=======
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    '''Create a view that will return a list of Items'''
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    '''Add a new item to the todo list'''
    # POST request
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    # GET request
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    '''Edit an existing item in the todo list'''
    item = get_object_or_404(Item, id=item_id)
    # POST request
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # GET request
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    '''Toggle the status of an item between done and not done'''
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    '''Delete an item from the todo list'''
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
>>>>>>> 389d879 (Switch back to sqllite for testing purposes)
