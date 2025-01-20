import pandas as pd

x = pd.DataFrame([['Delivering','Not Delivering','Delivering','Not Delivering','Delivering']], columns=['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday'])

def highlight_delivering(val):
    color = 'background-color: pink' if val == 'Delivering' else ''
    return color

xx = x.style.map(highlight_delivering)


