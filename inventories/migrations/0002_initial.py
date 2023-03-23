# Generated by Django 4.1.6 on 2023-03-19 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorygroup',
            name='items',
            field=models.ManyToManyField(blank=True, help_text='Enter items that belong in the inventory group.', to='items.item'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='user',
            field=models.OneToOneField(help_text='Enter user that owns the inventory (required).', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]