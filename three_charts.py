# three_charts.py

# adapted from: https://plot.ly/python/getting-started/#initialization-for-offline-plotting

import plotly
import plotly.graph_objs as go
#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) 

labels = []
values = []
for p in pie_data:
    labels.append(p["company"])
    values.append(p["market_share"])

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)# TODO: create a pie chart based on the pie_data

#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data

dates = []
prices = []
for p in line_data:
    dates.append(p["date"])
    prices.append(p["stock_price_usd"])

plotly.offline.plot({
    "data": [go.Scatter(x= dates, y= prices)],
    "layout": go.Layout(title="stock price over time")
}, auto_open=True)

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

genre = []
viewers = []
for a in bar_data:
    genre.append(a["genre"])
    viewers.append(a["viewers"])

plotly.offline.plot({
    "data": [go.Bar(x= viewers, y= genre, orientation="h")],
    "layout": go.Layout(title="viewers by genre")
}, auto_open=True)