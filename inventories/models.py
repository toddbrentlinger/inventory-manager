import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse

class Inventory(models.Model):
    # Fields
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text='Enter user that owns the inventory (required).')

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('inventory-detail-view', args=[str(self.id)])

class InventoryGroup(models.Model):
     # Fields

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, help_text='Enter inventory that the inventory group belongs to (required).')
    items = models.ManyToManyField('items.Item', blank=True, help_text='Enter items that belong in the inventory group.')
    name = models.CharField(max_length=50, blank=True, help_text='Enter name of the inventory group.')
    last_modified = models.DateTimeField(auto_now=True)

    # Metadata

    class Meta:
        ordering = ['name', '-last_modified']

    # Methods

    def __str__(self):
        return f'{self.inventory.user} ({self.name})'

    def get_absolute_url(self):
        return reverse('inventory-group-detail-view', args=[str(self.id)])
