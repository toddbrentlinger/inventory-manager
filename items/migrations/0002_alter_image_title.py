# Generated by Django 4.1.6 on 2023-02-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, help_text='Enter title of the image.', max_length=100),
        ),
    ]
