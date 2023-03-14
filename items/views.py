from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Item

class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item
    paginate_by = 25

class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item

@login_required
def item_detail_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    context = {
        item,
    }

    return render(request, 'items/item_detail.html', context=context)
