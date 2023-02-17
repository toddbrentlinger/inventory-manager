from django.contrib import admin
from .models import BorrowedItem, GiftedItem, Image, Item, SoldItem, ThrownAwayItem

admin.site.register(BorrowedItem)
admin.site.register(GiftedItem)
admin.site.register(Image)
admin.site.register(Item)
admin.site.register(SoldItem)
admin.site.register(ThrownAwayItem)
