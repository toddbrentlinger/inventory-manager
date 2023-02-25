from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:pk>/', views.user_detail_view, name='user-detail'),
]
