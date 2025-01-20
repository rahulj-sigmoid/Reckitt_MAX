import pandas as pd
import plotly.graph_objects as go

years = ['Before Route Optimization','After Route Optimization']
pallets_per_trip = [16.72, 18.34]
fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=pallets_per_trip,
    text=pallets_per_trip,
    textposition='outside',
    textfont=dict(color=['pink', 'hotpink']),
    marker_color=['pink', 'hotpink'],
    width=0.4
))
fig.update_layout(
    title={
        'text': "Route Optimization",
        'y': 0.88,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 15,
            'color': 'purple'
        }
    },
    annotations=[
        {
            'text': f"",
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
    xaxis = dict(tickfont=dict(color='purple'), titlefont=dict(color='purple')),
    yaxis = dict(title="Number of Pallets per Trip",
                 tickfont=dict(color='purple'), 
                 titlefont=dict(color='purple'),
                 range=[0, 20]),
    template='plotly_white',
    margin=dict(t=100, b=40),
    showlegend=False,
    bargap=1,
    width=500, height=400
)
#fig.show()