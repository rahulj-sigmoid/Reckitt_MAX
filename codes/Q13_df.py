import plotly.graph_objects as go
import pandas as pd
import json

data = pd.read_csv('./data/sales_states_total.csv')
xx = data[['State', 'Total POS Sales']].copy()