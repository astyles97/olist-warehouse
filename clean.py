import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt

load_dotenv()

engine = create_engine(os.environ['DATABASE'])

df = pd.read_sql("SELECT SUM(price) as gmv, seller_id "
                 "FROM raw.order_items "
                 "GROUP BY seller_id "
                 "ORDER BY SUM(price) DESC",
                 engine)

np.log10(df['gmv']).plot(kind='hist', bins=50)
plt.xlabel('log10(GMV)')
plt.ylabel('Sellers')
plt.show()
