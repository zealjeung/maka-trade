import os
path2 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener')
path3 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener\stockCaps')
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY, SATURDAY, SUNDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY
import plotly.offline as pyo
import plotly.graph_objs as go
from datetime import datetime


date1 = "2018-1-1"
date2 = "2018-11-29"
end_date = '11292018'
What_Stock1 = '^PSEi'

os.chdir(path2)
df = pd.read_csv('conso' + end_date + '.csv', index_col=0,
                 parse_dates=True, infer_datetime_format=True)
df = df[(df.index >= date1) & (df.index <= date2)]
df2 = df[df['TICKER'] == What_Stock1]

trace = go.Candlestick(x=df2.index,
                       open=df2.OPEN,
                       high=df2.HIGH,
                       low=df2.LOW,
                       close=df2.CLOSE)
data = [trace]

layout = go.Layout(title=What_Stock1, hovermode='closest',
                   font=dict(family='Courier New, monospace', size=18, color='#7f7f7f'))
config = {'scrollZoom': True}
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, config=config, filename='OHLCint ' + What_Stock1 + ' ' + end_date + '.html')
