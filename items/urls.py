from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='items'),
    path('<uuid:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
]
