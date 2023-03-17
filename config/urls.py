"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('inventories/', include('inventories.urls')),
    path('items/', include('items.urls')),
]

# Static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

# Media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
inventory-manager/ -> Home Site
inventory-manager/<username>/ -> User Page (displays user stats)
inventory-manager/<username>/inventory/ -> List of inventory groups and stats about each
inventory-manager/<username>/inventory/<InventoryGroup>/ -> List of items inside InventoryGroup with stats about each
inventory-manager/<username>/items/ -> List of all items in all inventory groups
inventory-manager/<username>/inventory/items/<ItemId>/ -> Detail about single item
'''