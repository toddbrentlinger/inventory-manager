import uuid
from django.db import models

class Inventory(models.Model):
    # Fields
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, help_text='Enter user that owns the inventory (required).')

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return self.id

class InventoryGroup(models.Model):
     # Fields

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, help_text='Enter inventory that the inventory group belongs to (required).')
    items = models.ManyToManyField('items.Item', blank=True, help_text='Enter items that belong in the inventory group.')
    name = models.CharField(max_length=50, blank=True, help_text='Enter name of the inventory group.')

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return self.id
