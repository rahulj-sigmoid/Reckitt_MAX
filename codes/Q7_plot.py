import pandas as pd
import plotly.express as px
import json

data = pd.read_csv('./data/birth_share.csv')
# Convert the data into a DataFrame
df = data.copy()
df['text'] = df['reckitt_birth_share'].apply(lambda x: str(int(round(x, 0)))+'%')
# Create the choropleth map
fig = px.choropleth(df,
                    locations='Hospital State',  # Column with state names
                    locationmode='USA-states',  # Use USA state codes for mapping
                    color='reckitt_birth_share',  # Color the states by the net hospitals won
                    title="Reckitt's Percentage Share in Births by State", 
                    color_continuous_scale=['red', 'yellow', 'green'],  # Customize the color scale
                    range_color=[0, 87], 
                    labels={'reckitt_birth_share': '% Share'},  # Label for the color scale
                    scope="usa",  # Focus on the United States
                    custom_data=['reckitt_birth_share', 'Hospital State', 'Net Total Births']
                    )


fig.update_layout(
    font=dict(
        size=9,  # Set the font size here
        color="black"
    )
)

fig.update_traces(
    hovertemplate=(
        '<b>State: %{customdata[1]}</b><br>' +
        'Reckitt Birth Share: %{customdata[0]:.2f}%<br>' +
        'Total Births: %{customdata[2]}'
    ), selector=dict(type='choropleth'),
)

for idx, row in df.iterrows():
    fig.add_scattergeo(
        locations=[row['Hospital State']],
        locationmode='USA-states',
        text=row['text'],          # Display state name
        mode='text',                # Show as text only
        showlegend=False, hoverinfo='none'
    )

fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})

# Show the plot
#fig.show()
