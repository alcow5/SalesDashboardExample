"""
# Small Business Sales Dashboard

A simple ETL pipeline and Power BI dashboard for small businesses to analyze sales trends. Features:

- CSV ingestion (monthly uploads)
- SQLite data storage
- Sales trend analysis via Power BI

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run ingestion: `python scripts/ingest_sales.py`
3. Run transform: `python scripts/transform_sales.py`
4. Connect Power BI to `sales_transformed` table in `sales.db`

"""
