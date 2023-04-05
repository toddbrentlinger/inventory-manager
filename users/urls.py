from django.urls import path
from . import views
from inventories.views import inventory_detail_view, inventorygroup_detail_view
from items.views import item_detail_view, item_list_view

urlpatterns = [
    path('<str:username>/', views.user_detail_view_username, name='user-detail'),
    path('<str:username>/inventory/', inventory_detail_view, name='inventory-detail'),
    path('<str:username>/inventory/<uuid:pk>/', inventorygroup_detail_view, name='inventorygroup-detail'),
    path('<str:username>/items/', item_list_view, name='items'),
    path('<str:username>/items/<uuid:pk>/', item_detail_view, name='item-detail'),
]

'''
inventory-manager/ -> Home Site
inventory-manager/<username>/ -> User Page (displays user stats)
inventory-manager/<username>/inventory/ -> List of inventory groups and stats about each
inventory-manager/<username>/inventory/<InventoryGroup>/ -> List of items inside InventoryGroup with stats about each
inventory-manager/<username>/items/ -> List of all items in all inventory groups
inventory-manager/<username>/inventory/items/<ItemId>/ -> Detail about single item
'''
