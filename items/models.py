import uuid
from django.db import models

class Image(models.Model):
    # Fields

    title = models.CharField(max_length=100, help_text='Enter title of the image (required).')

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return self.title

class Item(models.Model):
    # Fields

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, help_text='Enter name of item (required).')
    model_number = models.CharField(max_length=20, blank=True, help_text='Enter model number of item.')
    serial_number = models.CharField(max_length=20, blank=True, help_text='Enter serial number of the specific item.')
    description = models.TextField(blank=True, help_text='Enter description of the item.')
    price = models.ForeignKey('Price', on_delete=models.PROTECT, blank=True, null=True, help_text='Enter the price of the item.')
    purchase_date = models.DateField(blank=True, help_text='Enter date the item was purchased.')
    images = models.ManyToManyField(Image, blank=True, help_text='Enter any images of the item.')
    # slug? - used for url of item
    # state - Owned/InPossession, Borrowed, Gifted, Sold, ThrownAway

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return self.name

class Price(models.Model):
    # Fields

    currency = models.CharField(max_length=3, help_text='Enter 3-letter ISO 4217 alpha code, ex. USD or EUR (required).')
    amount = models.FloatField(help_text='Enter amount of the price in the selected currency\'s minor currency units, ex. cents (required).')

    # Metadata

    class Meta:
        pass

    # Methods

    def __str__(self):
        return f'${self.currency} ${self.amount}'
