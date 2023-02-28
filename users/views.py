from django.shortcuts import render, get_object_or_404
from .models import User
from inventories.models import Inventory
from items.models import BorrowedItem, Item

def index(request):
    '''View function for home page of site.'''

    # Generate counts of some of the main objects
    num_inventories = Inventory.objects.count()
    num_items = Item.objects.count()
    num_borrowed_items = BorrowedItem.objects.count()

    context = {
        'num_inventories': num_inventories,
        'num_items': num_inventories,
        'num_borrowed_items': num_inventories,
    }

    return render(request, 'index.html', context=context)

def user_detail_view(request, pk):
    '''Detail view for User model.'''

    user = get_object_or_404(User, pk=pk)

    context = {
        user,
    }

    return render(request, 'users/user_detail.html', context=context)
