from django.contrib import admin
from .models import BorrowedItem, Brand, GiftedItem, Image, Item, SoldItem, ThrownAwayItem

@admin.register(BorrowedItem)
class BorrowedItemAdmin(admin.ModelAdmin):
    list_display = ['item', 'action_type', 'reciever', 'date', 'return_promise_date', 'has_returned',]
    list_filter = ('date', 'action_type', 'has_returned',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(GiftedItem)
class GiftedItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ['images',]
    list_display = ['name', 'price_in_dollars', 'purchase_date', 'last_modified',]
    list_filter = ('purchase_date', 'last_modified',)

@admin.register(SoldItem)
class SoldItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ThrownAwayItem)
class ThrownAwayItemAdmin(admin.ModelAdmin):
    pass
