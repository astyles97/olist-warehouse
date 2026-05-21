import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text

load_dotenv()

engine = create_engine(os.environ['DATABASE'])

# customers = pd.read_csv('../data/raw/archive/olist_customers_dataset.csv')
# geolocation = pd.read_csv('../data/raw/archive/olist_geolocation_dataset.csv')
# order_items = pd.read_csv('../data/raw/archive/olist_order_items_dataset.csv')
# order_payments = pd.read_csv('../data/raw/archive/olist_order_payments_dataset.csv')
# order_reviews = pd.read_csv('../data/raw/archive/olist_order_reviews_dataset.csv')
# orders = pd.read_csv('../data/raw/archive/olist_orders_dataset.csv')


with engine.connect() as connection:
    result = connection.execute(text('SELECT version();'))
    print(result.scalar())