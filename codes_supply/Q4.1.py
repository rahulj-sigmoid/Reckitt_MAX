import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

categories = ["Pallets per trip before consolidation", "Pallets per trip after consolidation"]
values1 = [16.72, 21.32]
values2 = [16.72, 24.26]
categories_sla = ["SLA before consolidation", "SLA after consolidation"]
values3 = [99, 82]
values4 = [99, 74]

fig = make_subplots(rows=2, cols=2, subplot_titles=(
    "No. of Pallets - Order consolidation [+1 day]",
    "No. of Pallets - Order consolidation [+1 and +2 days]",
    "SLA - Order consolidation [+1 day]",
    "SLA - Order consolidation [+1 and +2 days]"), vertical_spacing=0.2,
                  horizontal_spacing=0.1)

fig.update_annotations(font_size=13)


colors = ['hotpink', 'purple']
fig.add_trace(go.Bar(x=categories, y=values1, marker_color=colors, text=values1, textposition='outside'), row=1, col=1)
fig.add_trace(go.Bar(x=categories, y=values2, marker_color=colors, text=values2, textposition='outside'), row=1, col=2)
fig.add_trace(go.Bar(x=categories_sla, y=values3, marker_color=colors, text=values3, textposition='outside'), row=2, col=1)
fig.add_trace(go.Bar(x=categories_sla, y=values4, marker_color=colors, text=values4, textposition='outside'), row=2, col=2)
fig.update_layout(yaxis1 = dict(range=[0, 30]))
fig.update_layout(yaxis2 = dict(range=[0, 30]))
fig.update_layout(yaxis3 = dict(range=[0, 120]))
fig.update_layout(yaxis4 = dict(range=[0, 120]))

fig.update_layout(
    title={
        'text': "Order Consolidation - Before / After",
        'xanchor': 'center',
        'yanchor': 'top',
        'y': 0.94,
        'x': 0.5,
        'font': {
            'size': 20,
            'color': 'hotpink'
        }
    },
    showlegend=False,
    height=600,
    width=900
)

fig.update_xaxes(tickangle=0, tickfont=dict(size=10))
fig.update_yaxes(tickfont=dict(size=10))

#fig.show()