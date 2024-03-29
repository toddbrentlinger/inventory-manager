import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse

class Inventory(models.Model):
    # Fields
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, help_text='Enter user that owns the inventory (required).')

    # Metadata

    class Meta:
        ordering = ['user__username',]

    # Methods

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('inventory-detail', args=[str(self.id)])
        return reverse('inventory-detail', kwargs={'username': self.user.username})
    
    def user_has_permission(self, user):
        '''Returns True if user has permission to view Inventory instance.'''
        return self.user == user

class InventoryGroup(models.Model):
     # Fields

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, help_text='Enter inventory that the inventory group belongs to (required).')
    items = models.ManyToManyField('items.Item', blank=True, help_text='Enter items that belong in the inventory group.')
    name = models.CharField(max_length=50, blank=True, help_text='Enter name of the inventory group.')
    #slug = models.SlugField(max_length=50, unique=True, null=False, help_text='Enter a url-safe, unique, lower-case version of the inventory group.')
    last_modified = models.DateTimeField(auto_now=True)

    # Metadata

    class Meta:
        ordering = ['name', '-last_modified']

    # Methods

    def __str__(self):
        return f'{self.inventory.user} ({self.name})'

    def get_absolute_url(self):
        #return reverse('inventorygroup-detail', args=[str(self.id)])
        return reverse('inventorygroup-detail', kwargs={'pk': str(self.id), 'username': self.inventory.user.username})
