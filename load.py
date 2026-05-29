import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text

load_dotenv(Path(__file__).parent / '.env')
engine = create_engine(os.environ['DATABASE'])

DATA_DIR = Path(__file__).parent / 'data' / 'raw' / 'archive'

# customers = pd.read_csv('data/raw/archive/olist_customers_dataset.csv')
# geolocation = pd.read_csv('data/raw/archive/olist_geolocation_dataset.csv')
# order_items = pd.read_csv('data/raw/archive/olist_order_items_dataset.csv')
# order_payments = pd.read_csv('data/raw/archive/olist_order_payments_dataset.csv')
# order_reviews = pd.read_csv('data/raw/archive/olist_order_reviews_dataset.csv')
# orders = pd.read_csv('data/raw/archive/olist_orders_dataset.csv')
# products = pd.read_csv('data/raw/archive/olist_products_dataset.csv')
# product_categories = pd.read_csv('data/raw/archive/product_category_name_translation.csv')

csv_to_table = {
    'olist_customers_dataset.csv': 'customers',
    'olist_geolocation_dataset.csv': 'geolocation',
    'olist_order_items_dataset.csv': 'order_items',
    'olist_order_payments_dataset.csv': 'payments',
    'olist_order_reviews_dataset.csv': 'reviews',
    'olist_orders_dataset.csv': 'orders',
    'olist_products_dataset.csv': 'products',
    'olist_sellers_dataset.csv': 'sellers',
    'product_category_name_translation.csv': 'category_translation',
}

for csv_file, table_name in csv_to_table.items():
    df = pd.read_csv(DATA_DIR / csv_file)
    df.to_sql(
        name=table_name,
        con=engine,
        schema='raw',
        if_exists='replace',
        index=False,
        method='multi',
        chunksize=10000,
    )

    print(f'Table {table_name} created successfully: {len(df):,} rows')