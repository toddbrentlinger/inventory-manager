from django.shortcuts import render, get_object_or_404
from .models import Inventory

def inventory_detail_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    context = {
        inventory,
    }

    return render(request, 'inventories/inventory_detail_html', context=context)
