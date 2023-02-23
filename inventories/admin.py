from django.contrib import admin
from .models import Inventory, InventoryGroup

# Inlines

class InventoryGroupInline(admin.TabularInline):
    extra = 0
    model = InventoryGroup

# Model Admins

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    inlines = [InventoryGroupInline, ]

@admin.register(InventoryGroup)
class InventoryGroupAdmin(admin.ModelAdmin):
    fields = ['inventory', 'name', 'items',]
    list_display = ['inventory', 'name',]
    list_filter = ['last_modified',]
