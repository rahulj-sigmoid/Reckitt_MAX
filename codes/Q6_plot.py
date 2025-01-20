import pandas as pd
import plotly.express as px

df = pd.read_csv('./data/renewals.csv')
temp = df.groupby(['Month', 'Current Contract Holder'], as_index=False).agg({'Hospital Name':'count', 
                                                                    'Net Total Births': 'sum'})
temp.columns = ['Month', 'Current Holder', 'Number of Contracts Expiring', 'Net Total Births']

# Load and prepare data
data = temp.copy()
data_sorted = data.sort_values('Month')

custom_colors = {
    'Abbott Exclusive': '#FFB6C1',  # Hot pink
    'MJN Exclusive': '#FF69B4',     # Light pink
    'Choice': '#FF1493',    # Deep pink
    'Other': 'purple'
    # Add more holders as needed with unique colors
}

# Create a stacked bar chart
fig = px.bar(data_sorted, 
             x='Month', 
             y='Number of Contracts Expiring', 
             color='Current Holder', 
             title='Number of Hospital Contracts Expiring by Month',
             labels={'Number of Contracts Expiring': '# Contracts Expiring', 'Month': 'Expiry Month'},
             barmode='stack', color_discrete_map=custom_colors)


for month in data_sorted['Month'].unique():
    month_data = data_sorted[data_sorted['Month'] == month]
    total_contracts = month_data['Number of Contracts Expiring'].sum()
    fig.add_annotation(
    x=month,  # Position annotation at the end of the stacked bar
    y=total_contracts,
    text=str(total_contracts),
    showarrow=False,
    font=dict(size=12, color="black"), xanchor="center",yanchor="bottom")
    
fig.update_layout(
    xaxis=dict(
        tickangle=45,  # Rotate the x-axis labels for better readability
        tickmode='array',  # Use an array for x-tick values
        tickvals=data_sorted['Month'],  # Explicitly define tick positions (all months will be shown)
        #ticktext=data_sorted['Month'] , # Display the actual month names as ticks
        tickfont=dict(color='hotpink'),
        title='Month', 
        titlefont=dict(color='black')), template='plotly_white',
    yaxis=dict(
        title='# Contracts Expiring', 
        titlefont=dict(color='black')))


# Show the plot
#fig.show()
