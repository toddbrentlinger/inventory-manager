import uuid
from django.db import models

class Person(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, help_text='Enter person\'s full name (required).')
    phone_number = models.CharField(max_length=10, blank=True, help_text='Enter person\'s full name.')
    email = models.EmailField(blank=True, help_text='Enter person\'s email.')
    thumbnail = models.ImageField(blank=True, help_text='Enter person\'s thumbnail image.')

    # Metadata
    class Meta:
        pass

    # Methods
    def __str__(self):
        return self.full_name
