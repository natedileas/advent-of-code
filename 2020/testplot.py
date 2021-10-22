import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
df = pd.read_csv('times.csv')

for col in ['Part 1', 'Part 2', 'Total']:
	df[col] = (pd.to_datetime(df[col], format="%M:%S") - pd.to_datetime('1900-01-01')).map(lambda td: td.total_seconds() / 60)

df['Total'][df['Part 1'].notna()] = pd.np.nan

print(df.head())

# fig = go.Figure(data=go.Bar(y=))
# fig = px.bar(df, x="Day", y= ['Part 1', 'Part 2', 'Total'])
fig = go.Figure(data=[
    go.Bar(name='Part 1', x=df['Day'], y=df['Part 1']),
    go.Bar(name='Part 2', x=df['Day'], y=df['Part 2']),
    go.Bar(name='Total', x=df['Day'], y=df['Total'])
])
# Change the bar mode
fig.update_layout(barmode='stack', 
	xaxis_title="Day",
    yaxis_title="Minutes",
    )
# fig.update_layout(barmode='stack')
# fig.write_html("testplotfile.html")
# fig.write_image("testimage.svg")
fig.show()