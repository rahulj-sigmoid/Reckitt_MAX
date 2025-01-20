import pandas as pd
import plotly.graph_objects as go
years = ["2022","2023"]
trips = [14890,15869]
text = ["14,890","15,869"]

increase_percentage = round((trips[1] - trips[0]) / (trips[0]) * 100,2)

fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=trips,
    text=text,
    textposition='outside',
    textfont=dict(color=['pink', 'hotpink']),
    marker_color=['pink', 'hotpink'],
    width=0.4
))
fig.update_layout(
    title={
        'text': "Number of Trips per Year",
        'y': 0.88,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 20,
            'color': 'purple'
        }
    },
    annotations=[
        {
            'text': f"Increase in number of Trips: {increase_percentage:.1f}%",
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 1.1,
            'showarrow': False,
            'font': {
                'size': 14,
                'color': 'purple'
            }
        }
    ],
    xaxis_title="Year",
    xaxis = dict(tickfont=dict(color='purple'), titlefont=dict(color='purple')),
    yaxis = dict(title="Number of Trips",
                 tickfont=dict(color='purple'), 
                 titlefont=dict(color='purple'),
                 range=[12000, 17000]),
    template='plotly_white',
    margin=dict(t=100, b=40),
    showlegend=False,
    bargap=1,
    width=500, height=400
)
#fig.show()