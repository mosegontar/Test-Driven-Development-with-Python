from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
def home_page(request):
    """Home page view function"""

    return render(request, 'home.html')

def view_list(request):
    """View list view function"""

    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    
    Item.objects.create(text=request.POST['item_text'])    
    return redirect('/lists/the-only-list-in-the-world/')
