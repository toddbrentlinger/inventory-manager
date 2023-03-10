# Generated by Django 4.1.6 on 2023-02-21 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='user',
            field=models.OneToOneField(help_text='Enter user that owns the inventory (required).', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
