from django.shortcuts import render, get_object_or_404
from .models import User
from inventories.models import Inventory
from items.models import BorrowedItem, Item

import datetime

def index(request):
    '''View function for home page of site.'''

    # Generate counts of some of the main objects
    
    num_inventories = Inventory.objects.count()
    num_items = Item.objects.count()
    num_borrowed_items = BorrowedItem.objects.count()

    # Adjust session variables
    
    # Increment number of visits
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Calculate time since last visited site
    datetime_timestamp_current = datetime.datetime.now().timestamp()
    datetime_timestamp_last_visited = request.session.get('datetime_timestamp_last_visited', datetime_timestamp_current)
    request.session['datetime_timestamp_last_visited'] = datetime_timestamp_current
    
    context = {
        'num_inventories': num_inventories,
        'num_items': num_items,
        'num_borrowed_items': num_borrowed_items,
        'num_visits': num_visits,
        'datetime_timestamp_last_visited': datetime_timestamp_last_visited,
    }

    return render(request, 'index.html', context=context)

def user_detail_view(request, pk):
    '''Detail view for User model.'''

    user = get_object_or_404(User, pk=pk)

    context = {
        user,
    }

    return render(request, 'users/user_detail.html', context=context)

def user_detail_view_username(request, username):
    '''Detail view for User model.'''

    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }

    return render(request, 'users/user_detail.html', context=context)

