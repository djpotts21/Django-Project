from django.shortcuts import render, redirect
from .models import Item


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
    #POST request
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'item_done' in request.POST
        Item.objects.create(name=name, done=done)
        return redirect('get_todo_list')

    #GET request
    return render(request, 'todo/add_item.html')
