from django.shortcuts import render, redirect
from .models import TodoListItem
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime

# Normal View of the webpage
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    date = datetime.now()
    formated_date = date.strftime("%d-%m-%Y")
    return render(request,'todolist.html',{'all_items':all_todo_items,'date':formated_date})


# Adding Items
def addTodoView(request):
    x = request.POST['content']
    if x == '':
        return HttpResponseRedirect('/')
    new_item = TodoListItem(item=x)
    new_item.save()
    messages.success(request,('Item has been Added!!'))
    return HttpResponseRedirect('/')


# Deleting Items
def deleteTodoView(request,i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    messages.success(request, ('Item has been Deleted!!'))
    return HttpResponseRedirect('/')


# Setting the item as completed
def cross_off(request,i):
    item = TodoListItem.objects.get(id = i)
    item.completed = True
    item.save()
    return redirect('home')


# Setting the item as not completed
def uncross(request,i):
    item = TodoListItem.objects.get(id = i)
    item.completed = False
    item.save()
    return redirect('home')


# to edit the item name
def edit(request,i):
    if request.method == 'POST':
        item = TodoListItem.objects.get(id = i)

        x = request.POST['content']
        item.item = x
        item.save()
        messages.success(request,('Item has been edited!!'))
        return redirect('home')

    else:
        item = TodoListItem.objects.get(id = i)
        return render(request, 'edit.html', {'item':item})