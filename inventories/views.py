from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Inventory, InventoryGroup

class InventoryListView(generic.ListView):
    model = Inventory
    paginate_by = 25

class InventoryDetailView(generic.DetailView):
    model = Inventory

def inventory_detail_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    # Check if user has access to inventory
    if request.user != inventory.user:
        raise PermissionDenied

    context = {
        'inventory': inventory,
        'user': request.user,
    }

    return render(request, 'inventories/inventory_detail.html', context=context)

class InventoryGroupDetailView(generic.DetailView):
    model = InventoryGroup

def inventory_group_detail_view(request, pk):
    inventory_group = get_object_or_404(InventoryGroup, pk=pk)

    context = {
        inventory_group,
    }

    return render(request, 'inventories/inventory_group_detail.html', context=context)
