from django.contrib import admin
from .models import Inventory, InventoryGroup

# admin.site.register(Inventory)
# admin.site.register(InventoryGroup)

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(InventoryGroup)
class InventoryGroupAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'name',]
    list_filer = ['last_modified',]
