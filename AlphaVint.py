# to load needed modules
import quandl  # financial data source
import pandas as pd  # for dataframe setup and csv loading
from datetime import datetime  # timse series: date convention
import matplotlib.pyplot as plt  # module for plotting
import os  # for input/output of files/directories
import plotly.offline as pyo
import plotly.graph_objs as go
from alpha_vantage.timeseries import TimeSeries

TICKER = 'EOD/AMZN'  # use either EOD or XNAS(datasets) / then ticker
TICKER2 = TICKER[-4:]  # change according to number of ticker characters
symbol = TICKER2
os.chdir(r'D:\Users\jong\PyProjects\Stocks\US Stocks')
key = open('alphavantage.txt', 'r').read()
ts = TimeSeries(key=key, output_format='pandas')
data = data, meta_data = ts.get_daily_adjusted(symbol=symbol,
                                               outputsize='full')
data = data.reset_index()
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
print(data.tail())

x = data.index
dfA = data['4. close']
y1 = dfA

Product_A = [go.Scatter(x=x,
                        y=y1,
                        mode='lines',  # 'markers+lines'
                        line={'width': 3, 'smoothing': 1.2},  # 'shape': 'spline'
                        name=TICKER2,
                        marker=dict(
                            size=3,
                            color='rgb(51,204,153)',
                            symbol='circle',
                            line={'width': 3}
                        ))]

data1 = Product_A
start = '2017-01-01'
end = '2018-11-09'
last = data.describe().loc['count', '4. close']

layout = go.Layout(title=TICKER2 + "  " + str(data['4. close'][-1]),
                   titlefont=dict(size=28, color='rgb(51,204,153)'),
                   xaxis=dict(showgrid=True, color='lightgray',
                              range=[start, end]),
                   yaxis=dict(title='$USD', showgrid=True, color='gray'),
                   hovermode='x')

fig = go.Figure(data=data1, layout=layout)
path3 = (r'D:\Users\jong\PyProjects\Stocks\US Stocks')
os.chdir(path3)
pyo.plot(fig, filename='USAlphaVint.html')
