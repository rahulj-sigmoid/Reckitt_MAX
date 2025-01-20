import plotly.graph_objects as go
import pandas as pd
import json

data = pd.read_csv('./data/worst_yoy_retailers.csv')
dff = data.rename(columns = {'sales_23_text':'POS Sales 2023 (till Oct)', 'sales_24_text':'POS Sales 2024 (till Oct)', 'YOY Growth Percentage (2024)': 'YoY Growth %'})
dff = dff[dff['yoy_growth']<0]
xx = dff[['Retailer', 'POS Sales 2023 (till Oct)', 'POS Sales 2024 (till Oct)',  'YoY Growth %']].copy()