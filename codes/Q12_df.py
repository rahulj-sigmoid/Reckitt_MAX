import plotly.graph_objects as go
import pandas as pd
import json

data = pd.read_csv('./data/sales_retailer_total.csv')
xx = data[['Retailer', 'Total POS Sales']].copy()