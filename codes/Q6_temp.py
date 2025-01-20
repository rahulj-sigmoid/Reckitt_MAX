import plotly.graph_objects as go
import pandas as pd

data = pd.read_excel('./data/win_loss_data.xlsx')
data = data.drop_duplicates(subset=['Hospital', 'Contract Status', 'Month Won or Lost'])[:-3]

x = data.groupby(['State', 'Contract Status'], as_index=False)['Hospital'].count()
xx = pd.pivot_table(x, index='State', columns='Contract Status', values='Hospital', aggfunc='sum').reset_index().rename_axis(None, axis=1)
xx = xx.fillna(0).copy()
xx.columns = ['State', 'Hospitals Lost', 'Hospitals Won']
xx['Net Hospitals Won'] = xx['Hospitals Won'] - xx['Hospitals Lost']

xx['Win Percentage'] = xx.apply(lambda row: round(row['Hospitals Won'] / (row['Hospitals Won'] + row['Hospitals Lost']) * 100, 1), axis=1)
xx = xx[['State','Hospitals Won','Hospitals Lost', 'Net Hospitals Won',
       'Win Percentage']]
xx = xx.sort_values('Hospitals Won', ascending=False)[:10].reset_index(drop=True)