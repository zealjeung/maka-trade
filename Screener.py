# plt.title('NET FOREIGN', color='purple', fontsize='large')
# Make sure you have run Append.py to update the conso database to latest
# To setup import modules and paths
import datetime
import os
path1 = (r'C:\Users\jong\PycharmProjects\Stocks\PSE screener\stockQuotes')
path2 = (r'C:\Users\jong\PycharmProjects\Stocks\PSE screener')
path3 = (r'C:\Users\jong\PycharmProjects\Stocks\PSE screener\stockCaps')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import style
# style.use('seaborn-dark')  # other choice: 'seaborn-pastel'

# Choose the stock and last trading date
What_Stock1 = 'ABA'
What_Stock2 = '^PSEi'
# i = f'{datetime.now():%m%d%Y}'
# end_date = str(i[:10])
end_date = ('10192018')

os.chdir(path2)
# load csv to a panda dataframe
df = pd.read_csv('conso' + end_date + '.csv')

# To convert Date object to Panda date format
df['DATE'] = pd.to_datetime(df.DATE)
# to add day of week column
df['DAY'] = df.DATE.dt.weekday_name

# make the dates column as index
df.set_index('DATE', inplace=True)
df2 = df[df['TICKER'] == What_Stock1]
#df2['RETURNS'] = df2['CLOSE'].pct_change(1)
#df2['Cum Ret'] = (1 + df2['RETURNS']).cumprod()
last = df2.describe().loc['count', 'CLOSE']
YTD = round((df.CLOSE[(int(last)) - 1] -
             df.CLOSE[0]) / df.CLOSE[0], 3) * 100.00

df3 = df[df['TICKER'] == What_Stock2]
#df3['RETURNS'] = df3['CLOSE'].pct_change(1)
#df3['Cum Ret'] = (1 + df3['RETURNS']).cumprod()

LastPrice = abs(df2.CLOSE[-1])
LastPrice2 = abs(df3.CLOSE[-1])
LastDate = str(df2.index[-1])
LD = LastDate[:10]
mean = round(df2.describe().loc['mean', 'CLOSE'], 2)

YTD2 = round((df2.CLOSE[(int(last)) - 1] -
              df2.CLOSE[0]) / df2.CLOSE[0], 3) * 100.00

# To show the 'AS OF DATE'
print(What_Stock1)
print('AS OF DATE:', LD)
print('YTD', YTD2, '% ')
print('Last Price = Php', LastPrice)
print('Mean = Php', mean)
print(df2.head())
print(df2.tail())

# to show additional/satistical info
stats = round(df2.describe()[df2.describe().columns[3:]], 2)

stats.index.name = 'Stats'
print(stats)
# set index name
df2.index.name = 'DATE'

# create graph of chosen symbol(1st chart Stock Prices)
# plt.figure(figsize=(21, 10.8))  # frameon=False).patch.set_visible(False)
# plt.subplots(sharex='all')
plt.subplot(5, 1, 1)
plt.subplot2grid((5, 1), (0, 0), rowspan=2, colspan=1)

plt.plot(df2.CLOSE, color='blue', linewidth=2.7)
plt.title('YTD STOCK PRICE', color='blue')
plt.xticks([])
# for dates, prices in df2.CLOSE.items():
plt.annotate(str(df2.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='blue', fontSize=15)
plt.legend([What_Stock1], loc='upper center', prop={'size': 25})

plt.subplot(5, 1, 3)
plt.plot(df3.CLOSE, color='darkgreen', linewidth=2.5)
plt.xticks([])
# plt.title(What_Stock2 + ' PERFORMANCE YTD')  # ,color='blue', fontsize='large')
# plt.xlabel('Dates')
# plt.ylabel('Tens of Billions')
# plt.grid(False)
# plt.ylim(0, 9000)
plt.annotate(str(df3.CLOSE[-1]), xy=(LastDate, LastPrice2),
             color='darkgreen', fontSize=15)
plt.legend(['PSEI'], loc='upper center')

# create graph of chosen symbol (2nd chart VOLUME)
plt.subplot(5, 1, 4)
plt.bar(df2.index, df2.VOLUME, color='turquoise')
# plt.xlabel('Dates')
plt.axis('on')
# plt.ylabel('in Tens of Billions')
# plt.title('VOLUME', color='turquoise', fontsize='large')
plt.grid(False)
plt.xticks([])
plt.legend(['Volume'], loc='upper center')
# create graph of chosen symbol (3nd chart NFB)
plt.subplot(5, 1, 5, facecolor='white')
plt.bar(df2.index, df2.NFB, color='purple')
# plt.xlabel('Dates')
plt.axis('on')
# plt.ylabel('Total PHP')
plt.grid(False)
plt.legend(['Net Foreign'], loc='upper center')
os.chdir(path3)
plt.savefig(end_date + What_Stock1 + '.svg', dpi=1200)
plt.show()

