from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:pk>/', views.inventory_detail_view, name='inventory-detail'),
]
