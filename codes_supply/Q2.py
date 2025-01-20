import pandas as pd
import plotly.graph_objects as go
data_dict = {"Cost_Type" : ['Inbound Transportation','Inbound Handling','Inventory Storage','Outbound Handling','Outbound Transportation','Cross Transfers',
                       'Administrative cost'],
        "2022" : [5.65,1.29,2.67,2.04,8.0,0.52,4.26],
        "2023" : [5.13,1.27,2.66,1.93,8.35,0.43,3.89]}


def format_with_m(value):
    if abs(value) >=1000000000:
        if value<0:
            return f"-${round(abs(value) / 1000000000, 2)}B"  # Format value as B, with one decimal place
        else:
            return f"+${round(abs(value) / 1000000000, 2)}B"  # Format value as B, with one decimal place
    elif abs(value) >= 1000000:
        if value<0:
            return f"-${round(abs(value) / 1000000, 2)}M"  # Format value as B, with one decimal place
        else:
            return f"+${round(abs(value) / 1000000, 2)}M"  # Format value as B, with one decimal place
            
    elif abs(value) >= 1000:
        if value<0:
            return f"-${round(abs(value) / 1000, 2)}K"  # Format value as B, with one decimal place
        else:
            return f"+${round(abs(value) / 1000, 2)}K"  # Format value as B, with one decimal place
    else:
        return f"${round(value, 2)}"
    

data = pd.DataFrame(data_dict)
data['2022_e'] = data['2022']*10**6
data['2023_e'] = data['2023']*10**6
data['diff_bw_years'] = data['2023_e'] - data['2022_e']
data['diff_bw_years_text'] = data['diff_bw_years'].apply(format_with_m)
#data['diff_bw_years_in_k'] = data['diff_bw_years_in_k'].astype(int)
data['perc_diff_bw_years'] = round(data['diff_bw_years'] / data['2022_e']*100,2)
data_sorted = data.sort_values(by='diff_bw_years',ascending=False)
cost_2022 = round(data_sorted['2022_e'].sum(),2)
cost_2023 = round(data_sorted['2023_e'].sum(),2)
cost_2022_text = format_with_m(cost_2022)[1:]
cost_2023_text = format_with_m(cost_2023)[1:]

cost_types = ["2022"] + data_sorted['Cost_Type'].to_list() + ["2023"]
costs = [cost_2022] + data_sorted['diff_bw_years'].to_list() + [cost_2023]
cost_texts = [cost_2022_text] + data_sorted['diff_bw_years_text'].to_list() + [cost_2023_text]  # In 1000s
fig = go.Figure(go.Waterfall(
    name="20",
    orientation="v",
    measure=["absolute", "relative", "relative", "relative", "relative", "relative", "relative", "relative", "absolute"],
    x=cost_types,
    y=costs,
    text=cost_texts,
    textfont=dict(color=['purple', 'red', 'hotpink','hotpink','hotpink','hotpink','hotpink','hotpink', 'purple']),
    textposition="outside",
    decreasing={"marker":{"color":"hotpink"}},
    increasing={"marker":{"color":"red"}},
    totals={"marker":{"color":"purple"}}
))


fig.update_layout(
    title={
        'text': "Cost Waterfall between 2022 and 2023",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {
            'size': 20,
            'color': 'purple'
        }
    },
    template='plotly_white',
    yaxis_title="Cost",
    xaxis_title="Year",
    xaxis=dict(
        ticks='inside',          # Display tick marks outside the plot
        tickwidth=2,              # Width of tick marks
        ticklen=10,                # Length of tick marks
        tickcolor = 'purple',
        tickangle=45,  # Rotate the x-axis labels for better readability
        tickmode='array',  # Use an array for x-tick values
        #tickvals= df['Month'],  # Explicitly define tick positions (all Quarters will be shown)
        #ticktext=df['Quarter']  # Display the actual Quarter names as ticks
        tickfont=dict(color='purple'),
    ),
    yaxis_range=[22500000, 26000000],
    showlegend=False,
    font=dict(
        size=12,
    ),
    margin=dict(t=100, b=40),
    waterfallgap=0.2,
)

#fig.show()
