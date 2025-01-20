import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv('./data/sales_vs_births.csv')


df = data.copy()
line_chart_sales = go.Scatter(
    x=df['Quarter'],
    y=df['total_sales'],
    mode='lines+markers+text',  # Add text labels on the markers
    name='POS Sales',
    line=dict(color='purple', width=2),  # Hot pink line color
    marker=dict(color='purple', size=5),  # Pink markers for the line
    text=df['POS_Sales_text'],  # Add text labels for the net Births won
    textposition='top center',  # Position the text above the markers
    textfont=dict(color='purple', size=10),  # Text color for the line chart labels
    customdata=df['POS_Sales_text'],
    hovertemplate='Quarter: %{x}<br>POS Sales: %{customdata}<extra></extra>'
)

# Create a line chart for Net Births Won on a rolling basis with labels
line_chart = go.Scatter(
    x=df['Quarter'],
    y=df['Running_Net'],
    mode='lines+markers+text',  # Add text labels on the markers
    name='Rolling Net Births Won',
    line=dict(color='hotpink', width=2),  # Hot pink line color
    marker=dict(color='hotpink', size=5),  # Pink markers for the line
    text=df['Running_Net_text'],  # Add text labels for the net Births won
    textposition='top center',  # Position the text above the markers
    textfont=dict(color='hotpink', size=10),  # Text color for the line chart labels
    customdata = df['Running_Net_text'],
    hovertemplate='Quarter: %{x}<br>Net Rolling Births Won: %{customdata}<extra></extra>'
)

# Create the figure and add the bar and line charts
fig = go.Figure(data=[line_chart_sales, line_chart])

# Update layout with dual y-axes
fig.update_layout(
    title='Quarterly POS Sales versus Net Rolling Births Won',
    title_font=dict(size=18, color='hotpink'),
    yaxis_title='Net Rolling Births Won',
    yaxis=dict(
        title='Net Rolling Births Won',
        range=[0, 350000],
        titlefont=dict(size=14, color='hotpink'),
        tickfont=dict(size=12, color='pink')
    ),
    # Define second y-axis for the net hospitals won line chart
    yaxis2=dict(
        range=[0, 600000000],
        title='POS Sales',
        titlefont=dict(size=14, color='purple'),
        tickfont=dict(size=12, color='purple'),
        overlaying='y',  # Overlays the second axis on the same plot
        side='right',  # Place the second axis on the right
        showgrid=False  # Optionally hide the grid on the right axis
    ),
    plot_bgcolor='white',  # Set the background color to white
    template='plotly_white',  # Use a white template for a clean appearance
    legend_title="Births and Sales Data",
    xaxis=dict(
        ticks='inside',          # Display tick marks outside the plot
        tickwidth=2,              # Width of tick marks
        ticklen=10,                # Length of tick marks
        tickcolor = 'hotpink',
        tickangle=45,  # Rotate the x-axis labels for better readability
        tickmode='array',  # Use an array for x-tick values
        #tickvals= df['Month'],  # Explicitly define tick positions (all Quarters will be shown)
        #ticktext=df['Quarter']  # Display the actual Quarter names as ticks
        tickfont=dict(color='hot pink'),
        title='Quarter', 
        titlefont=dict(color='black'),
    ),
    showlegend=True,
    legend=dict(
        x=1.1,  # Move the legend outside the plot area
        y=1.0,  # Position it at the top-right of the chart
        orientation='v',  # Arrange the legend items vertically
        title='',  # Set the legend title
        traceorder='normal'  # Display legend items in the order of appearance
    )
)

# Add the secondary y-axis to the line chart (using yaxis2)
fig.update_traces(
    selector=dict(name="POS Sales"),
    yaxis="y2"  # Assign the line chart to the second y-axis
)
# Show the plot
#fig.show()
