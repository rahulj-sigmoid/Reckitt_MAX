import pandas as pd
df = pd.read_csv('./data/renewals.csv')
temp = df.groupby(['Month', 'Current Contract Holder'], as_index=False).agg({'Hospital Name':'count', 
                                                                    'Net Total Births': 'sum'})
temp.columns = ['Month', 'Current Holder', '# Contracts Expiring', 'Total Births']
g = pd.pivot_table(temp, index='Month', columns='Current Holder', values=['# Contracts Expiring', 
                                                                              'Total Births'], 
                   aggfunc='sum').swaplevel(axis=1).sort_index(level=0, axis=1).reindex(['# Contracts Expiring', 'Total Births'], 
                                                                                        level=1, axis=1).rename_axis(columns=[None, None]).reset_index()
xx = g.fillna(0).copy()