from django.shortcuts import render,redirect
from .models import List, Deleted
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item added successfully')
            return render(request,'home.html',{'all_items':all_items})

    else:
        all_items = List.objects.all
        return render(request,'home.html',{'all_items':all_items})

def about(request):
    return render(request,'about.html')

## home section delete view
def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    p = Deleted(item=item.item,completed=item.completed)
    p.save()
    item.delete()
    messages.success(request, 'Item Deleted successfully')
    return redirect('home')

def restore(request,list_id):
    item = Deleted.objects.get(pk=list_id)
    p = List(item=item.item,completed=item.completed)
    p.save()
    item.delete()
    messages.success(request, 'Item Restored successfully')
    return redirect('deleted')

## deleted section delete view
def delete1(request,list_id):
    item = Deleted.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item Deleted successfully')
    return redirect('deleted')

def cross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def deleted(request):
    all_items = Deleted.objects.all
    return render(request,'deleted.html',{'all_items':all_items})
    


def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request,list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)
        form = ListForm(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Edited successfully')
            return redirect('home')

    else:
        item = List.objects.get(pk = list_id)
        return render(request,'edit.html',{'item': item})

## delete all for home section

def delete_all(request):
    List.objects.all().delete()
    messages.success(request, 'Items Deleted successfully')
    return redirect('home')

def delete1_all(request):
    Deleted.objects.all().delete()
    messages.success(request, 'Items Deleted successfully')
    return redirect('home')

def complete_all(request):
    all_items = List.objects.all()
    for things in all_items:
        print("hello")
        things.completed = True
        things.save()
        print("world")
    messages.success(request,'All Tasks Completed')
    return redirect('home')
