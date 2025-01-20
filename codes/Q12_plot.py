import plotly.graph_objects as go

import pandas as pd


z = pd.read_csv('./data/sales_retailer_monthly.csv')
top_5 = ['Walmart', 'Kroger', 'Target', 'Costco', 'HEB']

def format_with_m(value):
    if value >=1000000000:
        return f"${round(value / 1000000000, 2)}B"  # Format value as B, with one decimal place
    elif value >= 1000000:
        return f"${round(value / 1000000, 2)}M"  # Format value as M, with one decimal place
    elif value>=1000:
        return f"${round(value / 1000, 2)}K"  # Format value as K, with one decimal place
    else:
        return f"${round(value, 2)}"
    

# Sample data
months = z['date']
brand_1_sales = z[top_5[0]]
brand_1_text = z[top_5[0]].apply(format_with_m)
brand_2_sales = z[top_5[1]]
brand_2_text = z[top_5[1]].apply(format_with_m)
brand_3_sales = z[top_5[2]]
brand_3_text = z[top_5[2]].apply(format_with_m)
brand_4_sales = z[top_5[3]]
brand_4_text = z[top_5[3]].apply(format_with_m)
brand_5_sales = z[top_5[4]]
brand_5_text = z[top_5[4]].apply(format_with_m)

# Create scatter plots
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=months, y=brand_1_sales, customdata=brand_1_text, mode='lines+markers', name=top_5[0], marker=dict(color='red'),
    hovertemplate='<b>Walmart</b><br>Month: %{x}<br>Sales: %{customdata}<extra></extra>'  # Customize hover text
))
              
fig.add_trace(go.Scatter(
    x=months, y=brand_2_sales, customdata=brand_2_text, mode='lines+markers', name=top_5[1], marker=dict(color='purple'),
    hovertemplate='<b>Kroger</b><br>Month: %{x}<br>Sales: %{customdata}<extra></extra>'
))
fig.add_trace(go.Scatter(
    x=months, y=brand_3_sales, customdata=brand_3_text, mode='lines+markers', name=top_5[2], marker=dict(color='lightpink'),
    hovertemplate='<b>Target</b><br>Month: %{x}<br>Sales: %{customdata}<extra></extra>'
))
fig.add_trace(go.Scatter(
    x=months, y=brand_4_sales, customdata=brand_4_text, mode='lines+markers', name=top_5[3], marker=dict(color='magenta'),
    hovertemplate='<b>Costco</b><br>Month: %{x}<br>Sales: %{customdata}<extra></extra>'
))
fig.add_trace(go.Scatter(
    x=months, y=brand_5_sales, customdata=brand_5_text, mode='lines+markers', name=top_5[4], marker=dict(color='hotpink'),
    hovertemplate='<b>HEB</b><br>Month: %{x}<br>Sales: %{customdata}<extra></extra>'
))

# Add title and labels
fig.update_layout(
    title='Monthly Sales of Top 5 Retailers',
    title_font=dict(size=18, color='hotpink'),
    yaxis= dict(title='POS Sales', titlefont = dict(color='black'), tickfont=dict(color='black')),
    showlegend=True,
    xaxis=dict(
        tickangle=45,  # Rotate the x-axis labels for better readability
        tickmode='array',  # Use an array for x-tick values
        tickfont=dict(color='black'),
        title='Month', 
        titlefont=dict(color='black'),
    ),
    template='plotly_white'
)

# Show the plot
#fig.show()
