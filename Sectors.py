import datetime
import os
path1 = (r'C:\Users\jong\PycharmProjects\Stocks\PSE screener\stockQuotes')
path2 = (r'C:\Users\jong\PycharmProjects\Stocks\PSE screener')
path3 = (r'C:\Users\jong\PycharmProjects\Stocks\PSE screener\stockCaps')
import pandas as pd
import matplotlib.pyplot as plt

What_Stock1 = '^PSEi'
What_Stock2 = '^INDUSTRIAL'
What_Stock3 = '^SERVICE'
What_Stock4 = '^MINING-OIL'
What_Stock5 = '^HOLDING'
What_Stock6 = '^PROPERTY'
What_Stock7 = '^FINANCIAL'
# i = f'{datetime.now():%m%d%Y}'
# end_date = str(i[:10])
end_date = ('10312018')
os.chdir(path2)

df = pd.read_csv('conso' + end_date + '.csv')
df['DATE'] = pd.to_datetime(df.DATE)
df['DAY'] = df.DATE.dt.weekday_name
df.set_index('DATE', inplace=True)
df2 = df[df['TICKER'] == What_Stock1]
df3 = df[df['TICKER'] == What_Stock2]
LastPrice2 = abs(df3.CLOSE[-1])
df4 = df[df['TICKER'] == What_Stock3]
LastPrice3 = abs(df4.CLOSE[-1])
df5 = df[df['TICKER'] == What_Stock4]
LastPrice4 = abs(df5.CLOSE[-1])
df6 = df[df['TICKER'] == What_Stock5]
LastPrice5 = abs(df6.CLOSE[-1])
df7 = df[df['TICKER'] == What_Stock6]
LastPrice6 = abs(df7.CLOSE[-1])
df8 = df[df['TICKER'] == What_Stock7]
LastPrice7 = abs(df8.CLOSE[-1])

# PSEI
LastPrice = abs(df2.CLOSE[-1])
LastDate = str(df2.index[-1])
LastDateYTDs = str(df2.index[0])
LastDateYTD = str(df2.index[12])
LastDateP = str(df2.index[6])
LD = LastDate[:10]
mean = round(df2.describe().loc['mean', 'CLOSE'], 2)
last = df2.describe().loc['count', 'CLOSE']
YTD = round((df2.CLOSE[(int(last)) - 1] -
             df2.CLOSE[0]) / df2.CLOSE[0], 3) * 100.00

plt.figure(figsize=(20, 10))
plt.subplot(7, 1, 1, facecolor='w')
plt.plot(df2.CLOSE, color='blue', linewidth=3)
plt.title('SECTOR RANKINGS ' + str(end_date), color='grey')
plt.xticks([])
plt.annotate(" " + str(df2.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='blue', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='blue', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='blue', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='blue', fontSize=15)
plt.legend([What_Stock1], loc='upper center', prop={'size': 14})

LastPrice = abs(df3.CLOSE[-1])
LastDate = str(df3.index[-1])
LastDateYTDs = str(df3.index[0])
LastDateYTD = str(df3.index[12])
LastDateP = str(df3.index[6])
LD = LastDate[:10]
mean = round(df3.describe().loc['mean', 'CLOSE'], 2)
last = df3.describe().loc['count', 'CLOSE']
YTD = round((df3.CLOSE[(int(last)) - 1] -
             df3.CLOSE[0]) / df3.CLOSE[0], 4) * 100.00

plt.subplot(7, 1, 2, facecolor='w')
plt.plot(df3.CLOSE, color='darkgreen', linewidth=2)
plt.xticks([])
plt.annotate(" " + str(df3.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='darkgreen', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='darkgreen', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='darkgreen', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='darkgreen', fontSize=15)
plt.legend([What_Stock2], loc='upper center')

LastPrice = abs(df4.CLOSE[-1])
LastDate = str(df4.index[-1])
LastDateYTDs = str(df4.index[0])
LastDateYTD = str(df4.index[12])
LastDateP = str(df4.index[6])
LD = LastDate[:10]
mean = round(df4.describe().loc['mean', 'CLOSE'], 2)
last = df4.describe().loc['count', 'CLOSE']
YTD = round((df4.CLOSE[(int(last)) - 1] -
             df4.CLOSE[0]) / df4.CLOSE[0], 5) * 100.00

plt.subplot(7, 1, 3, facecolor='w')
plt.plot(df4.CLOSE, color='coral', linewidth=2)
plt.xticks([])
plt.annotate(" " + str(df4.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='coral', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='coral', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='coral', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='coral', fontSize=15)
plt.legend([What_Stock3], loc='upper center')

LastPrice = abs(df5.CLOSE[-1])
LastDate = str(df5.index[-1])
LastDateYTDs = str(df5.index[0])
LastDateYTD = str(df5.index[12])
LastDateP = str(df5.index[6])
LD = LastDate[:10]
mean = round(df5.describe().loc['mean', 'CLOSE'], 2)
last = df5.describe().loc['count', 'CLOSE']
YTD = round((df5.CLOSE[(int(last)) - 1] -
             df5.CLOSE[0]) / df5.CLOSE[0], 5) * 100.00

plt.subplot(7, 1, 5, facecolor='w')
plt.plot(df5.CLOSE, color='cornflowerblue', linewidth=2)
plt.xticks([])
plt.annotate(" " + str(df5.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='cornflowerblue', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='cornflowerblue', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='cornflowerblue', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='cornflowerblue', fontSize=15)
plt.legend([What_Stock4], loc='upper center')
plt.grid(False)

LastPrice = abs(df6.CLOSE[-1])
LastDate = str(df6.index[-1])
LastDateYTDs = str(df6.index[0])
LastDateYTD = str(df6.index[12])
LastDateP = str(df6.index[6])
LD = LastDate[:10]
mean = round(df6.describe().loc['mean', 'CLOSE'], 2)
last = df6.describe().loc['count', 'CLOSE']
YTD = round((df6.CLOSE[(int(last)) - 1] -
             df6.CLOSE[0]) / df6.CLOSE[0], 5) * 100.00

plt.subplot(7, 1, 6, facecolor='w')
plt.plot(df6.CLOSE, color='sienna', linewidth=2)
plt.xticks([])
plt.annotate(" " + str(df6.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='sienna', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='sienna', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='sienna', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='sienna', fontSize=15)
plt.legend([What_Stock5], loc='upper center')

LastPrice = abs(df7.CLOSE[-1])
LastDate = str(df7.index[-1])
LastDateYTDs = str(df7.index[0])
LastDateYTD = str(df7.index[12])
LastDateP = str(df7.index[6])
LD = LastDate[:10]
mean = round(df7.describe().loc['mean', 'CLOSE'], 2)
last = df7.describe().loc['count', 'CLOSE']
YTD = round((df7.CLOSE[(int(last)) - 1] -
             df7.CLOSE[0]) / df7.CLOSE[0], 4) * 100.00

plt.subplot(7, 1, 4, facecolor='w')
plt.plot(df7.CLOSE, color='c', linewidth=2)
plt.xticks([])
plt.annotate(" " + str(df7.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='c', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='c', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='c', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='c', fontSize=15)
plt.legend([What_Stock6], loc='upper center')

LastPrice = abs(df8.CLOSE[-1])
LastDate = str(df8.index[-1])
LastDateYTDs = str(df8.index[0])
LastDateYTD = str(df8.index[12])
LastDateP = str(df8.index[6])
LD = LastDate[:10]
mean = round(df8.describe().loc['mean', 'CLOSE'], 2)
last = df8.describe().loc['count', 'CLOSE']
YTD = round((df8.CLOSE[(int(last)) - 1] -
             df8.CLOSE[0]) / df8.CLOSE[0], 4) * 100.00

plt.subplot(7, 1, 7, facecolor='w')
plt.plot(df8.CLOSE, color='darkorchid', linewidth=2)
# plt.xticks([])
plt.annotate(" " + str(df8.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='darkorchid', fontSize=10)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='darkorchid', fontSize=15)
plt.annotate(' %', xy=(LastDateP, LastPrice),
             color='darkorchid', fontSize=15)
plt.annotate(YTD, xy=(LastDateYTD, LastPrice),
             color='darkorchid', fontSize=15)
plt.legend([What_Stock7], loc='upper center')

os.chdir(path3)
plt.savefig(end_date + What_Stock1 + '.png', dpi=1200)
plt.show()
