import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
df = pd.read_sql_query("SELECT * FROM sales_transformed LIMIT 5", conn)
print(df.columns)
conn.close()