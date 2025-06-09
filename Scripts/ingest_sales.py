import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite DB (or Snowflake if desired)
engine = create_engine('sqlite:///sales.db')

def ingest_csv(file_path):
    df = pd.read_csv('data/more_sample_sales.csv', parse_dates=['Date'])
    df.to_sql('sales_raw', engine, if_exists='replace', index=False)
    print("Data ingested into sales_raw table")

if __name__ == '__main__':
    ingest_csv('../data/more_sample_sales.csv')
