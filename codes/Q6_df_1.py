import pandas as pd
df = pd.read_csv('./data/renewals.csv')
xx = df.drop('Month', axis=1).sort_values(['Contract Expiry Date', 'Net Total Births'], ascending=[True, False]).reset_index(drop=True)