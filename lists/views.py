from django.shortcuts import render, redirect
from lists.models import Item, List

# Create your views here.
def home_page(request):
    """Home page view function"""

    return render(request, 'home.html')

def view_list(request, list_id):
    """View list view function"""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)    
    return redirect('/lists/{}/'.format(list_.id))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/{}/'.format(list_.id))