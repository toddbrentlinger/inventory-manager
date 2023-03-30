from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item
from users.models import User

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    paginate_by = 25

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

@login_required
def item_list_view(request, pk):
    user = get_object_or_404(User, pk=pk)

    # Check if user has access to inventory
    if request.user != user:
        raise PermissionDenied
    
    # TODO: Continue...
    user_items = []

@login_required
def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    # Check if user has access to inventory
    if request.user != item.inventory.user:
        raise PermissionDenied

    context = {
        item,
    }

    return render(request, 'items/item_detail.html', context=context)

class ItemCreate(CreateView):
    model = Item
    fields = [
        'inventory', 'name', 'model_number', 'serial_number', 'brand', 
        'description', 'price', 'purchase_date', 'images',
    ]

class ItemUpdate(UpdateView):
    model = Item
    fields = [
        'inventory', 'name', 'model_number', 'serial_number', 'brand', 
        'description', 'price', 'purchase_date', 'images',
    ]
    
class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('index')
