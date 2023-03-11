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

    def has_view_permission(self, request, obj=None):
        if self.model.user != request.user:
            return False
        
        return super().has_view_permission(request, obj)

@admin.register(InventoryGroup)
class InventoryGroupAdmin(admin.ModelAdmin):
    fields = ['inventory', 'name', 'items',]
    filter_horizontal = ['items',]
    list_display = ['inventory', 'name', 'item_count',]
    list_filter = ['last_modified',]

    @admin.display(description='Items')
    def item_count(self, obj):
        return obj.items.count()
