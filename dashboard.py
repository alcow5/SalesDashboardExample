import streamlit as st
import pandas as pd
import sqlite3

# Connect to DB
@st.cache_data
def load_data():
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql_query("SELECT * FROM sales_transformed", conn)
    conn.close()
    return df

df = load_data()

# Sidebar filters

st.sidebar.title("Filters")

selected_year = st.sidebar.multiselect(
    "Select Year", options=sorted(df['Year'].unique()), default=df['Year'].unique()
)

selected_product = st.sidebar.multiselect(
    "Select Product", options=sorted(df['Product'].unique()), default=df['Product'].unique()
)

selected_region = st.sidebar.multiselect(
    "Select Region", options=sorted(df['Region'].unique()), default=df['Region'].unique()
)

selected_month = st.sidebar.multiselect(
    "Select Month", options=sorted(df['Month'].unique()), default=df['Month'].unique()
)

filtered_df = df[
    df['Year'].isin(selected_year) &
    df['Product'].isin(selected_product) &
    df['Region'].isin(selected_region) &
    df['Month'].isin(selected_month)
]
# Main title
st.title("📊 Sales Dashboard")

# KPIs
st.subheader("Key Metrics")
col1, _ = st.columns(2)
col1.metric("Total Revenue", f"${filtered_df['Sales_Amount'].sum():,.2f}")

# Monthly Revenue Trend
st.subheader("Monthly Revenue Trend")
trend = filtered_df.groupby(['Year', 'Month'])['Sales_Amount'].sum().reset_index()
trend['Month'] = pd.to_datetime(trend['Year'].astype(str) + "-" + trend['Month'].astype(str))
trend = trend.sort_values('Month')

st.line_chart(trend.set_index("Month")['Sales_Amount'])

# Revenue by Product
st.subheader("Revenue by Product")
product_rev = filtered_df.groupby('Product')['Sales_Amount'].sum().sort_values(ascending=False)
st.bar_chart(product_rev)
