import plotly.graph_objects as go
import pandas as pd
data = pd.read_excel('./data/win_loss_data.xlsx')
data = data.drop_duplicates(subset=['Hospital', 'Contract Status', 'Month Won or Lost'])[:-3]
temp = data[data['Contract Status']=='Lost'].drop('Contract Status', axis=1).copy()
temp.columns = ['Hospital', 'City', 'State', 'Total Births', 'Lost To', 'Month Lost']
temp['Month Lost'] = temp['Month Lost'].apply(lambda x: x.date())
temp['Hospital'] = temp['Hospital'].apply(lambda x: x.split(',')[0])
xx = temp.copy().sort_values('Total Births', ascending=False).reset_index(drop=True)