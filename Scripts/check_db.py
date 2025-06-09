import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Preview a few rows from sales_clean
print("\nSample rows from sales_clean:")
for row in cursor.execute("SELECT * FROM sales_transformed LIMIT 5;"):
    print(row)

conn.close()