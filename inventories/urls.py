from django.urls import path
from . import views

urlpatterns = [
    path('', views.InventoryListView.as_view(), name='inventories'),
    #path('<uuid:pk>/', views.InventoryDetailView.as_view(), name='inventory-detail'),
    #path('<uuid:pk>/', views.inventory_detail_view, name='inventory-detail'),
    path('groups/<uuid:pk>', views.InventoryGroupDetailView.as_view(), name='inventorygroup-detail'),
]
