import pandas as pd
import datetime as dt
import numpy as np

INPUT_FILE = "Online Retail.xlsx" 
OUTPUT_FILE = "rfm_scores.csv"
print(f"Starting RFM Analysis on: {INPUT_FILE}")

try:
    df = pd.read_excel(INPUT_FILE)
except FileNotFoundError:
    print(f"Error: File not found. Please make sure {INPUT_FILE} is in the same folder.")
    exit()
df.dropna(subset=['CustomerID'], inplace=True)
df['CustomerID'] = df['CustomerID'].astype(int)
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
max_date = df['InvoiceDate'].max()
NOW = max_date + dt.timedelta(days=1)
rfm_r = df.groupby('CustomerID', as_index=False)['InvoiceDate'].max()
rfm_r['Recency'] = (NOW - rfm_r['InvoiceDate']).dt.days
rfm_r = rfm_r[['CustomerID', 'Recency']]
rfm_fm = df.groupby('CustomerID').agg(
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('TotalPrice', 'sum')
).reset_index()

rfm_df = rfm_r.merge(rfm_fm, on='CustomerID')
rfm_df.to_csv(OUTPUT_FILE, index=False)
print(f"RFM Data saved to: {OUTPUT_FILE}")
print("\nRFM Data Sample:")
print(rfm_df.head())