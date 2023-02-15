from django.shortcuts import render, get_object_or_404
from .models import Inventory, InventoryGroup

def inventory_detail_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    context = {
        inventory,
    }

    return render(request, 'inventories/inventory_detail_html', context=context)

def inventory_group_detail_view(request, pk):
    inventory_group = get_object_or_404(InventoryGroup, pk=pk)

    context = {
        inventory_group,
    }

    return render(request, 'inventories/inventory_group_detail.html', context=context)
