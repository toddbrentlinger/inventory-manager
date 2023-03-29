from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='items'),
    path('create/', views.ItemCreate.as_view(), name='item-create'),
    path('<uuid:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('<uuid:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('<uuid:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
]
