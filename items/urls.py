from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
]
