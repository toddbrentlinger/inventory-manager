from django.urls import path
from . import views
from inventories.views import inventory_detail_view, inventorygroup_detail_view
from items.views import item_detail_view, item_list_view

urlpatterns = [
    path('<uuid:pk>/', views.user_detail_view, name='user-detail'),
    path('<uuid:pk>/inventory/', inventory_detail_view, name='inventory-detail'),
    path('<uuid:pk>/inventory/<slug:inventorygroup>/', inventorygroup_detail_view, name='inventorygroup-detail'),
    path('<uuid:pk>/items/', item_list_view, name='items'),
    path('<uuid:pk>/items/<uuid:item_pk>/', item_detail_view, name='item-detail'),
]

'''
inventory-manager/ -> Home Site
inventory-manager/<username>/ -> User Page (displays user stats)
inventory-manager/<username>/inventory/ -> List of inventory groups and stats about each
inventory-manager/<username>/inventory/<InventoryGroup>/ -> List of items inside InventoryGroup with stats about each
inventory-manager/<username>/items/ -> List of all items in all inventory groups
inventory-manager/<username>/inventory/items/<ItemId>/ -> Detail about single item
'''
