import pandas as pd
import json
states = json.load(open("states.json", 'rb'))
abb = dict(map(reversed, states.items()))
data = pd.read_csv('./data/birth_share.csv')
data.columns = ['State', 'Reckitt Births', 'Total Births', '% Birth Share Reckitt']
data['State'] = data['State'].map(abb)
xx = data.dropna().sort_values('% Birth Share Reckitt', ascending=False).reset_index(drop=True)
xx['% Birth Share Reckitt'] = xx['% Birth Share Reckitt'].apply(lambda x: str(x)+'%')