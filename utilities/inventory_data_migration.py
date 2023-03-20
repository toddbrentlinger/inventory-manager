from decouple import config
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

        self.User = apps.get_model('users', 'User')

def initialize_database(apps, schema_editor):
    models = Models(apps)

def main():
    # By default the first sheet is imported, returning Pandas.DataFrame object
    df = read_ods(config('TOOL_INVENTORY_SPREADSHEET_FILE_LOCATION'))

    # Print Pandas.DataFrame object containing ODS file spreadsheet
    print(df)

if __name__ == '__main__':
    main()
