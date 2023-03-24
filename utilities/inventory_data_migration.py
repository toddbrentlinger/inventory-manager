from decouple import config
from django.conf import settings
from django.core.files.base import ContentFile
from pandas_ods_reader import read_ods

import pandas as pd
import re
import requests

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

        self.User = apps.get_model('users', 'User')

def add_model_inst_list_to_field(m2m_field, model_inst_list):
    '''
    Adds list of model instances to ManyToManyField.

    Parameters:
        m2m_field (ManyToManyField):
        model_inst_list (Model[]):
    '''
    for model_inst in model_inst_list:
        model_inst.save()
        m2m_field.add(model_inst)

def initialize_database(apps, schema_editor):
    models = Models(apps)
    brands = [
        'Anvil',
        'Bessey',
        'Bosch',
        'Buck Bros',
        'Comoware',
        'Craftsman',
        'Dewalt',
        'Diablo',
        'Empire',
        'Estwing',
        'Firm Grip',
        'Flexzilla',
        'Freud',
        'Goodjob',
        'Husky',
        'Irwin Tools',
        'Jastind',
        'Klein Tools',
        'Metabo',
        'Milescraft',
        'Narex',
        'Pony',
        'Ruitool',
        'Stanley',
        'Sungator',
        'Swanson',
        'Yoselin',
    ]

    # Create two test users to add items to their inventory and save them to the database
    user1 = models.User.objects.create_user('user1', 'user1@mail.com', 'password1')
    user2 = models.User.objects.create_user('user2', 'user2@mail.com', 'password2')

    # Create Inventory for each user
    inventory1 = models.Inventory.objects.create(user=user1)
    inventory2 = models.Inventory.objects.create(user=user2)

    # Create "Tools" InventoryGroup for each inventory to fill with tool Items
    toolGroup1 = models.InventoryGroup(inventory=inventory1, name='Tools')
    toolGroup2 = models.InventoryGroup(inventory=inventory2, name='Tools')

    # Dictionary to hold model instances for ManyToManyFields.
    # Key is field name and value is list of model instances.
    # After other fields in Item instance are set and it's saved to database,
    # can then add to the actual ManyToManyFields.
    # NOTE: One dict for each user's InventoryGroup
    inventorygroup_m2m_instances_dict = [
        { 'items': [], },
        { 'items': [], },
    ]

    # Import tool inventory spreadsheet ODS file, returning Pandas.DataFrame object
    df = read_ods(config('TOOL_INVENTORY_SPREADSHEET_FILE_LOCATION'))

    # Filter rows where "Tool" index is NOT None
    df_filtered = list(filter(lambda row: row[1] is not None, df.itertuples()))

    # Half of items assigned to each user
    user1_number_items = len(df_filtered) // 2

    for index, row in enumerate(df_filtered):
        # Create Item object
        item = models.Item()

        # Dictionary to hold model instances for ManyToManyFields.
        # Key is field name and value is list of model instances.
        # After other fields in Item instance are set and it's saved to database,
        # can then add to the actual ManyToManyFields.
        item_m2m_instances_dict = {
            'images': [],
        }

        # Inventory (ForeignKey)
        # Add tool Item to first or second Users Inventory
        item.inventory = inventory1 if index < user1_number_items else inventory2

        # Name (Char)
        item.name = row[1]

        # Model Number (Char)
        item.model_number = row[2] if row[2] is not None else ''

        # Serial Number (Char)

        # Brand (ForeignKey) - Check with brands array for known brands
        for brand in brands:
            if re.search(f'(?<![a-z0-9]){ brand }(?![a-z0-9])', row[1], re.I):
                # Get or create Brand model instance
                item.brand = models.Brand.objects.get_or_create(
                    name=brand
                )

        # Description (Text)

        # Price (Integer) - number of American cents
        # Skip if value is NaN or null using pandas library
        if pd.notna(row[3]):
            item.price = row[3] * 100

        # Purchase Date - (Date)
        # TODO: Keep variable of last purchase date for items with same 
        # purchase date in combined data cells

        # Images - (ManyToMany)
        # TODO: Use requests library to access image from url
        response = requests.get(row[4])
        if response.status_code == 200:
            image_content = ContentFile(response.content)
            item_m2m_instances_dict['images'].append(image_content)

        # Save Item object to database
        item.save()

        # Now that Item is saved to database, add ManyToManyFields
        add_model_inst_list_to_field(item.images, item_m2m_instances_dict['images'])

        # Add tool Item to first or second Users "Tools" InventoryGroup
        if index < user1_number_items:
            inventorygroup_m2m_instances_dict[0]['items'].append(item)
        else:
            inventorygroup_m2m_instances_dict[1]['items'].append(item)

    # Save "Tool" InventoryGroup objects to database
    toolGroup1.save()
    toolGroup2.save()

    # Now that InventoryGroup is saved to database, add ManyToManyFields
    add_model_inst_list_to_field(toolGroup1.items, inventorygroup_m2m_instances_dict[0]['items'])
    add_model_inst_list_to_field(toolGroup2.items, inventorygroup_m2m_instances_dict[1]['items'])

def main():
    # By default the first sheet is imported, returning Pandas.DataFrame object
    df = read_ods(config('TOOL_INVENTORY_SPREADSHEET_FILE_LOCATION'))

    # Print Pandas.DataFrame object containing ODS file spreadsheet
    print(df)

    # https://developer-docs.amazon.com/amazon-business/docs/product-search-api-v1-reference
    params = {
        'keywords': 'Dewalt 20V MAX* ½ in. Cordless Drill/Driver'
    }
    response = requests.get(
        "https://na.business-api.amazon.com/products/2020-08-26/products",
        params=params
    )
    print(response.json())

if __name__ == '__main__':
    main()
