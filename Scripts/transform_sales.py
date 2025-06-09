import sqlite3
import pandas as pd

def transform():
    conn = sqlite3.connect('sales.db')

    df = pd.read_sql_query("SELECT * FROM sales_raw", conn)

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Add year and month columns
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()

    # Save transformed data
    df.to_sql('sales_transformed', conn, if_exists='replace', index=False)
    conn.close()

transform()