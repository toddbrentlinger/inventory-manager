from decouple import config
from django.contrib.auth import get_user_model
from pandas_ods_reader import read_ods

import pandas as pd

class Models:
    def __init__(self, apps):
        # Cannot import models directly as it may be a newer version
        # than this migration expects. Use historical versions instead.
        
        # Inventories app

        self.Inventory = apps.get_model('inventories', 'Inventory')
        self.InventoryGroup = apps.get_model('inventories', 'InventoryGroup')
        
        # Items app

        self.BorrowedItem = apps.get_model('items', 'BorrowedItem')
        self.Brand = apps.get_model('items', 'Brand')
        self.GiftedItem = apps.get_model('items', 'GiftedItem')
        self.Image = apps.get_model('items', 'Image')
        self.Item = apps.get_model('items', 'Item')

        # Users

        self.User = get_user_model()

def initialize_database(apps, schema_editor):
    models = Models(apps)

    # Create two test users to add items to their inventory and save them to the database
    user1 = models.User.objects.create_user('user1', 'user1@mail.com', 'password1')
    user2 = models.User.objects.create_user('user2', 'user2@mail.com', 'password2')

    # Import tool inventory spreadsheet ODS file, returning Pandas.DataFrame object
    df = read_ods(config('TOOL_INVENTORY_SPREADSHEET_FILE_LOCATION'))

    # Filter rows where "Tool" index is NOT None
    df_filtered = list(filter(lambda row: row[1] is not None, df.itertuples()))

    # Half of items assigned to each user
    user1_number_items = len(df_filtered) // 2

    for index, row in enumerate(df_filtered):
        # Create Item object
        item = models.Item()

        # Inventory
        # Name
        # Model Number
        # Serial Number
        # Brand
        # Description
        # Price
        # Purchase Date
        # Images

        # Dictionary to hold model instances for ManyToManyFields.
        # Key is field name and value is list of model instances.
        # After other fields in Item instance are set and it's saved to database,
        # can then add to the actual ManyToManyFields.
        manytomany_instances_dict = {
            'images': [],
        }

        # Save Item object to database
        item.save()

        # Now that Item is saved to database, add ManyToManyFields

def main():
    # By default the first sheet is imported, returning Pandas.DataFrame object
    df = read_ods(config('TOOL_INVENTORY_SPREADSHEET_FILE_LOCATION'))

    # Print Pandas.DataFrame object containing ODS file spreadsheet
    print(df)

if __name__ == '__main__':
    main()
