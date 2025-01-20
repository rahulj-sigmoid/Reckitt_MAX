# Data
import pandas as pd
import plotly.graph_objects as go

years = ["2022", "2023"]
volumes = [275490, 262320]
volumes_in_k = [vol/10**3 for vol in volumes]
text = [str(vol) + "K" for vol in volumes_in_k]
decrease_percentage = ((volumes[0] - volumes[1]) / volumes[0]) * 100

fig = go.Figure()
fig.add_trace(go.Bar(
    x=years,
    y=volumes_in_k,
    text=text,
    textposition='outside',
    textfont=dict(color=['pink', 'hotpink']),
    marker_color=['pink', 'hotpink'],
    width=0.4
))
fig.update_layout(
    title={
        'text': "Number of Pallets",
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
            'text': f"Decrease in Volume: {decrease_percentage:.1f}%",
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
    yaxis = dict(title="Volume",
                 tickfont=dict(color='purple'), 
                 titlefont=dict(color='purple'),
                 tickformat=",.0f",
                 ticksuffix="K",
                 range=[0, 350]),
    template='plotly_white',
    margin=dict(t=100, b=40),
    showlegend=False,
    bargap=1,
    width=500, height=400
)
#fig.show()