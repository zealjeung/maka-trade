import os
path2 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener')
path3 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener\stockCaps')
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY, SATURDAY, SUNDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY

date1 = "2018-1-1"
date2 = "2018-11-08"
end_date = '11292018'
What_Stock1 = 'NOW'

os.chdir(path2)
df = pd.read_csv('conso' + end_date + '.csv', index_col=0,
                 parse_dates=True, infer_datetime_format=True)
df = df[(df.index >= date1) & (df.index <= date2)]
df2 = df[df['TICKER'] == What_Stock1]

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
dayFormatter = DateFormatter('%Y-%m-%d')

fig, ax = plt.subplots()  # figsize=(21, 10.8)
fig.subplots_adjust(bottom=0.5)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_major_formatter(dayFormatter)
# ax.xaxis.set_major_locator(mdates.AutoDateLocator())


candlestick_ohlc(ax, zip(mdates.date2num(df2.index.to_pydatetime()),
                         df2['OPEN'], df2['HIGH'],
                         df2['LOW'], df2['CLOSE']),
                 width=.7, colorup='g', alpha=.9)

ax.xaxis_date()
ax.autoscale_view()
plt.title([What_Stock1], color='k')
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
os.chdir(path3)
plt.savefig(end_date + What_Stock1 + '.svg', dpi=1200)
plt.show()
