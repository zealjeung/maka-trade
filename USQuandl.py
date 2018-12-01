# to load needed modules
import quandl  # financial data source
import pandas as pd  # for dataframe setup and csv loading
from datetime import datetime  # timse series: date convention
import matplotlib.pyplot as plt  # module for plotting
from matplotlib import style  # customizing graphs
style.use('seaborn-pastel')  # specify style
import os  # for input/output of files/directories


# to research the ticker symbol of us stocks
dftick = pd.read_html(
    'https://www.marketwatch.com/tools/markets/stocks/country/united-states/7')
# change the last digit(page of url) to scan thru the ticker list
print(dftick[0])

# Input database/ticker url:https://docs.quandl.com/docs/data-organization
TICKER = 'EOD/AAPL'  # use either EOD or XNAS(datasets) / then ticker
TICKER2 = TICKER[-4:]  # change according to number of ticker characters

# Date Option 1 - use this only if current day is weekday(-1 converted to US)
i = str(datetime.now())
end_date = str(i[:10])
# Date Option 2 - input desired end_date
# end_date = '2018-08-17'

# to align api version with desired date
api_version = end_date

# to config request of data from quandl
# read my quandl api key  stored in a .txt file
os.chdir(r'D:\Users\jong\PyProjects\Stocks\US Stocks')
quandl.ApiConfig.api_key = open('quandl.txt', 'r').read()
quandl.ApiConfig.api_version = api_version
# change desired stock price start_date
Stock = quandl.get(TICKER, start_date='2018-01-01',
                   end_date=end_date, authtoken=quandl.ApiConfig.api_key)

# to print all wanted info
print(Stock.shape)
print(Stock.columns)
print(TICKER)
print(Stock.describe())

os.chdir(r'D:\Users\jong\PyProjects\Stocks\US Stocks')
# to store data from quandl to a file and open it as dataframe
Stock.to_csv(TICKER2 + ' ' + end_date + '_ohlc.csv')
df = pd.read_csv(TICKER2 + ' ' + end_date + '_ohlc.csv', header=0,
                 parse_dates=True)
df['Date'] = pd.to_datetime(df.Date)
df.set_index('Date', inplace=True)
print(df.tail())
LastDate = str(df.index[-1])
LD = LastDate[:10]
# show graph
plt.figure(figsize=(21, 10.8))
plt.plot(df.Close, linewidth=3, color='orange')
# plt.xlabel('Dates')
plt.ylabel('Close ($USD)', fontSize=12)
plt.title('YTD PERFORMANCE')
plt.grid(False)
plt.annotate(str(df.Close[-1]), xy=(i, df.Close[-1]),
             color='orange', fontSize=15)
plt.legend([TICKER2], loc='upper center', prop={'size': 25})
plt.savefig(end_date + ' ' + TICKER2 + '.png')
plt.show()


print(TICKER2)
print('AS OF DATE:', LD)
last = df.describe().loc['count', 'Close']
int(last)
YTD = (df.Close[(int(last)) - 1] -
       df.Close[0]) / df.Close[0]*100
# To show YTD performance to date
print('YTD', round(YTD, 2), '%')
print(df.tail())
