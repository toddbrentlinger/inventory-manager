from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:pk>/', views.item_detail_view, name='item-detail'),
]
