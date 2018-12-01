# to load needed modules
import quandl  # financial data source
import pandas as pd  # for dataframe setup and csv loading
from datetime import datetime  # timse series: date convention
import matplotlib.pyplot as plt  # module for plotting
import os  # for input/output of files/directories
import plotly.offline as pyo
import plotly.graph_objs as go

# to research the ticker symbol of us stocks
dftick = pd.read_html(
    'https://www.marketwatch.com/tools/markets/stocks/country/united-states/7')
# change the last digit(page of url) to scan thru the ticker list
# print(dftick[0])

# Input database/ticker url:https://docs.quandl.com/docs/data-organization
TICKER = 'EOD/AAPL'  # use either EOD or XNAS(datasets) / then ticker
TICKER2 = TICKER[-4:]  # change according to number of ticker characters

# Date Option 1 - use this only if current day is weekday(-1 converted to US)
i = str(datetime.now())
end_date = str(i[:10])
# Date Option 2 - input desired end_date
# end_date = '2018-08-17'

from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
os.chdir(r'D:\Users\jong\PyProjects\Stocks\US Stocks')
key = open('alphavantage.txt', 'r').read()
ts = TimeSeries(key=key, output_format='pandas')
data = data, meta_data = ts.get_daily_adjusted(symbol='AMZN',
                                               outputsize='full')
data = data.reset_index()
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
print(data.tail())

plt.figure(figsize=(21, 10.8))
plt.plot(data['4. close'], linewidth=1.5, color='turquoise')
plt.plot(data['4. close'], linewidth=1.5, color='turquoise')
plt.ylabel('Close ($USD)', fontSize=12)
plt.title('YTD PERFORMANCE')
plt.grid(True, color='snow', linewidth=.25)
plt.annotate("      " + str(data['4. close'][-1]), xy=(i, data['4. close'][-1]),
             color='turquoise', fontSize=25)
plt.legend([TICKER2], loc='upper center', prop={'size': 20})
path3 = (r'D:\Users\jong\PyProjects\Stocks\US Stocks')
os.chdir(path3)
plt.savefig(end_date + ' ' + TICKER2 + '.svg', dpi=1200)
plt.show()
