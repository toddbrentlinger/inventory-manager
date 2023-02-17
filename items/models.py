import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Abstract Models

class ActionItem(models.Model):
    # Fields

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.OneToOneField('Item', on_delete=models.CASCADE, help_text='Enter item associated with the action.')
    date = models.DateField(blank=True, null=True, help_text='Enter date action occurred.')
    reason = models.TextField(blank=True, help_text='Enter the reason for taking the action with the item.')
    notes = models.TextField(blank=True, help_text='Enter any notes about the action.')

    # Metadata

    class Meta:
        abstract = True

    # Methods

    def __str__(self):
        return f'${self.id} - ${self.item}'

class RecipientActionItem(ActionItem):
    # Enumerations

    class RecipientActionType(models.TextChoices):
        BORROWED = 'BRWD', _('Borrowed')
        GIFTED = 'GFTD', _('Gifted')
        SOLD = 'SLD', _('Sold')

    # Fields

    reciever = models.ForeignKey('people.Person', on_delete=models.RESTRICT, help_text='Enter person who recieved the item.')
    action_type = models.CharField(
        max_length=4,
        choices=RecipientActionType.choices,
        default=RecipientActionType.BORROWED 
    )

    # Metadata

    class Meta(ActionItem.Meta):
        abstract = True

    # Methods

    def __str__(self):
        pass

# Concrete Models

class BorrowedItem(RecipientActionItem):
    # Fields

    return_promise_date = models.DateField(help_text='Enter date item is to be returned.')
    has_returned = models.BooleanField(default=False, help_text='Has item been returned?')

    # Metadata

    class Meta(RecipientActionItem.Meta):
        pass

    # Methods

    def __str__(self):
        pass

class GiftedItem(RecipientActionItem):
    # Fields

    # Metadata

    class Meta(RecipientActionItem.Meta):
        pass

    # Methods

    def __str__(self):
        pass

class Image(models.Model):
    # Fields

    # TODO: Can access height and width of image_file without opening file. Should remove width and height fields since they're not neccesary.
    # Field 'title' can also be accessed inside image_file, however the name is the file name including directories and file type.
    image_file = models.ImageField(
        upload_to='uploads/images/%Y/%m/%d/',
        storage=None, # TODO: Setup storage object https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.storage
        # width_field='width', 
        # height_field='height', 
        help_text='Enter image file.'
    )
    # width = models.SmallIntegerField(editable=False)
    # height = models.IntegerField(editable=False)
    title = models.CharField(max_length=100, help_text='Enter title of the image (required).')

    # Metadata

    class Meta:
        ordering = ['title']

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
    price = models.IntegerField(blank=True, help_text='Enter price of item in American cents (ex. $23.56 => 2356).')
    # price = models.ForeignKey('Price', on_delete=models.PROTECT, blank=True, null=True, help_text='Enter the price of the item.')
    purchase_date = models.DateField(blank=True, help_text='Enter date the item was purchased.')
    images = models.ManyToManyField(Image, blank=True, help_text='Enter any images of the item.')
    # slug? - used for url of item
    # state - Owned/InPossession, Borrowed, Gifted, Sold, ThrownAway
    last_modified = models.DateTimeField(auto_now=True)

    # Metadata

    class Meta:
        ordering = ['name', '-purchase_date']

    # Methods

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail-view', args=[str(self.id)])

class SoldItem(RecipientActionItem):
    # Fields

    # Metadata

    class Meta(RecipientActionItem.Meta):
        pass

    # Methods

    def __str__(self):
        pass

class ThrownAwayItem(ActionItem):
    # Fields

    # Metadata

    class Meta(ActionItem.Meta):
        pass

    # Methods

    def __str__(self):
        pass
