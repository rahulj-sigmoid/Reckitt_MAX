import plotly.graph_objects as go
import pandas as pd
import json
states = json.load(open("states.json", 'rb'))
abb = dict(map(reversed, states.items()))
data = pd.read_excel('./data/opportunity.xlsx')
opp = pd.pivot_table(data, index='Hospital State', columns='Hospital Type', values='Net Total Births', aggfunc='count').reset_index().rename_axis(None, axis=1)
zz = opp.fillna(0)
zz['Total Cities'] = zz['100% Abbott Exclusive City'] + zz['100% Choice Exclusive City']+ zz['100% MJN Exclusive City'] +  zz['Abbott Dominant City'] + zz['Choice Dominant City'] + zz['Opportunity'] + zz['Reckitt Dominant City']
zz = zz[['Hospital State', 'Opportunity', 'Total Cities']]
zz['Hospital State'] = zz['Hospital State'].map(abb)
zz = zz.dropna()
zz.columns = ['State', 'Cities tagged Opportunity', 'Total Cities']
xx = zz.copy().sort_values('Cities tagged Opportunity', ascending=False).reset_index(drop=True)