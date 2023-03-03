from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Item

class ItemDetailView(generic.DetailView):
    model = Item

def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    context = {
        item,
    }

    return render(request, 'items/item_detail.html', context=context)
