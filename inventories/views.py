from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Inventory, InventoryGroup

class InventoryListView(LoginRequiredMixin, generic.ListView):
    model = Inventory
    paginate_by = 25

class InventoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Inventory

@login_required
def inventory_detail_view_old(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)

    # Check if user has access to inventory
    if request.user != inventory.user:
        raise PermissionDenied

    context = {
        'inventory': inventory,
    }

    return render(request, 'inventories/inventory_detail.html', context=context)

@login_required
def inventory_detail_view(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    inventory = get_object_or_404(Inventory, user=user)

    context = {
        'inventory': inventory,
    }

    return render(request, 'inventories/inventory_detail.html', context=context)


class InventoryGroupDetailView(LoginRequiredMixin, generic.DetailView):
    model = InventoryGroup

@login_required
def inventorygroup_detail_view(request, pk):
    inventorygroup = get_object_or_404(InventoryGroup, pk=pk)

    context = {
        inventorygroup,
    }

    return render(request, 'inventories/inventorygroup_detail.html', context=context)
