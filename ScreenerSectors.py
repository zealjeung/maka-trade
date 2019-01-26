# ScreenerSerctor file shows a selected stock to be featured and will be compared against PSEi and all other Index Sector

import os
import datetime as datetime
import matplotlib.pyplot as plt
import pandas as pd

# Edit these paths first
# Where is your csv located?
path2 = (r'C:\Users\...) 
# Where you want to save the output file?
path3 = (r'C:\Users\...) 

# Choose the stock and last trading date
What_Stock = 'ISM'
Index = '^PSEi'
end_date = ('01252019')  # i = f'{datetime.now():%m%d%Y}'end_date = str(i[:10])
os.chdir(path2)
# load csv to a panda dataframe
df = pd.read_csv('conso' + end_date + '.csv')
df['DATE'] = pd.to_datetime(df.DATE)
# make the dates column as index
df.set_index('DATE', inplace=True)
df2 = df[df['TICKER'] == What_Stock]
last = df2.describe().loc['count', 'CLOSE']
YTD = round((df.CLOSE[(int(last)) - 1]
             - df.CLOSE[0]) / df.CLOSE[0], 3) * 100.00
df3 = df[df['TICKER'] == Index]
MP = abs(df2.describe().loc['mean', 'CLOSE'])
MP2 = abs(df3.describe().loc['mean', 'CLOSE'])
LP = abs(df2.CLOSE[-1])
LP2 = abs(df3.CLOSE[-1])
MD = str(df2.index[2])
LastDate = str(df2.index[-1])
LD = LastDate[:10]
mean = round(df2.describe().loc['mean', 'CLOSE'], 2)
YTD2 = round((df2.CLOSE[(int(last)) - 1] -
              df2.CLOSE[0]) / df2.CLOSE[0], 3) * 100.00
anno = str(round(df2.describe().loc['mean', 'CLOSE'],2))
anno3 = str(round(df3.describe().loc['mean', 'CLOSE'],2))


#print commands
print(What_Stock)
print('AS OF DATE:', LD)
print('YTD', YTD2, '% ')
print('Last Price = Php', LP)
print('Mean = Php', mean)
print(df2.head())
print(df2.tail())
desc = df2.describe()
stats = round(desc[desc.columns[3:]], 2)
stats.index.name = 'Stats'
print(stats)
df2.index.name = 'DATE'


plt.rc('axes',edgecolor='snow')
plt.rc_context({'ytick.color':'gray'})
plt.subplot2grid((6, 2), (0, 0), rowspan=2, colspan=1)
plt.plot(df2.CLOSE, color='dodgerblue', linewidth=1.4)
plt.title('Investa Stock Trendings' +
          ' (wk' + str(end_date) + ')', color='blue')
plt.xticks([])
# plt.yticks([])
plt.axis('on')
plt.annotate('       ' + str(df2.CLOSE[-1]),
             xy=(LD, LP), color='dodgerblue', fontSize=10)
plt.legend([What_Stock], loc='upper center', prop={'size': 10})
plt.axhline(df2.describe().loc['mean', 'CLOSE'], color = 'gray', alpha = .4, linewidth = 1.2, linestyle = '--')
plt.annotate(('meanline' + ' ' + anno), xy=(MD, MP), color='gray', fontSize=8)
plt.grid(color='snow', linewidth=2.5)

# plt.subplot(6, 1, 3)
plt.subplot2grid((6, 2), (2, 0), rowspan=2, colspan=1)
plt.plot(df3.CLOSE, color='darkgreen', linewidth=1)
plt.xticks([])
plt.yticks([])
plt.axis('on')
plt.grid(color='snow', linewidth=2.5)
plt.annotate('         ' + str(df3.CLOSE[-1]), xy=(LD, LP2),
                              color='darkgreen', fontSize=8)
plt.legend(['PSEI'], loc='upper center',prop={'size': 8})
plt.axhline(round(df3.describe().loc['mean', 'CLOSE'], 2),
                             color='gray', alpha=.4, linewidth=1.2, linestyle='--')
plt.annotate(('meanline' + ' ' + anno3), xy=(MD, MP2), color='gray', fontSize=8)

# create graph of chosen symbol (2nd chart VOLUME)
plt.subplot2grid((6, 2), (4, 0), rowspan=1, colspan=1)
plt.bar(df2.index, df2.VOLUME, color='turquoise', linewidth=1)
plt.axis('on')
plt.grid(False)
plt.xticks([])
plt.yticks([])
plt.legend(['Volume'], loc='upper center',prop={'size': 7})
plt.axhline(round((df2.describe().loc['mean', 'VOLUME'] * 1.1), 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')
# create graph of chosen symbol (3nd chart NFB)
# plt.subplot(6, 1, 6, facecolor='white')
plt.rc_context({'xtick.color':'gray'})
plt.subplot2grid((6, 2), (5, 0), rowspan=1, colspan=1)
plt.bar(df2.index, df2.NFB, color='purple', linewidth=1)
plt.axis('on')
plt.yticks([])
plt.grid(False)
plt.legend(['Net Foreign'], loc='upper center',prop={'size': 7})

IND='^INDUSTRIAL'
SER='^SERVICE'
MIN='^MINING-OIL'
HOL='^HOLDING'
PRO='^PROPERTY'
FIN='^FINANCIAL'
# i = f'{datetime.now():%m%d%Y}'
# i = str(datetime.now())
# end_date1 = str(i[:10])
# end_date = ('12202018')
os.chdir(path2)

df=pd.read_csv('conso' + end_date + '.csv')
df['DATE']=pd.to_datetime(df.DATE)
df.set_index('DATE', inplace=True)
df2=df[df['TICKER'] == IND]
LastPrice1=abs(df3.CLOSE[-1])
df3=df[df['TICKER'] == SER]
LastPrice2=abs(df3.CLOSE[-1])
df4=df[df['TICKER'] == MIN]
LastPrice3=abs(df4.CLOSE[-1])
df5=df[df['TICKER'] == HOL]
LastPrice4=abs(df5.CLOSE[-1])
df6=df[df['TICKER'] == PRO]
LastPrice5=abs(df6.CLOSE[-1])
df7=df[df['TICKER'] == FIN]
LastPrice6=abs(df7.CLOSE[-1])

LastPrice=abs(df2.CLOSE[-50])
LastDate=str(df2.index[-1])
LastDateYTDs=str(df2.index[0])
LastDateYTD=str(df2.index[12])
LastDateP=str(df2.index[6])
LD=LastDate[:10]
mean=round(df2.describe().loc['mean', 'CLOSE'], 2)
last=df2.describe().loc['count', 'CLOSE']
YTD=round((df2.CLOSE[(int(last)) - 1]
             - df2.CLOSE[0]) / df2.CLOSE[0] * 100, 2)

plt.rc('axes',edgecolor='snow')
# plt.figure(figsize=(20, 10))
# plt.subplot(6, 2, 1) #rows,colums,position
plt.subplot2grid((6, 2), (0, 1), rowspan=1, colspan=1)
plt.plot(df2.CLOSE, color='fuchsia', linewidth=1)
plt.title('SECTOR RANKINGS ' + str(end_date), color='gray')
plt.xticks([])
plt.axis('off')
plt.annotate("         " + str(df2.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='fuchsia', fontSize=8)
plt.annotate('YTD   ', xy=(LastDateYTDs, LastPrice),
             color='fuchsia', fontSize=8)
plt.annotate('   %', xy=(LastDateP, LastPrice),
             color='fuchsia', fontSize=8)
plt.annotate('    ' + str(YTD), xy=(LastDateYTD, LastPrice),
             color='fuchsia', fontSize=8)
plt.legend([IND], loc='upper center', prop={'size': 7})
plt.axhline(round(df2.describe().loc['mean', 'CLOSE'], 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')

LastPrice=abs(df3.CLOSE[-50])
LastDate=str(df3.index[-1])
LastDateYTDs=str(df3.index[0])
LastDateYTD=str(df3.index[12])
LastDateP=str(df3.index[6])
LD=LastDate[:10]
mean=round(df3.describe().loc['mean', 'CLOSE'], 2)
last=df3.describe().loc['count', 'CLOSE']
YTD=round((df3.CLOSE[(int(last)) - 1]
             - df3.CLOSE[0]) / df3.CLOSE[0] * 100, 2)

# plt.subplot(6, 2, 2, facecolor='w')
plt.subplot2grid((6, 2), (2, 1), rowspan=1, colspan=1)
plt.plot(df3.CLOSE, color='olivedrab', linewidth=1)
plt.xticks([])
plt.axis('off')
plt.annotate("         " + str(df3.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='olivedrab', fontSize=8)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='olivedrab', fontSize=8)
plt.annotate('    %', xy=(LastDateP, LastPrice),
             color='olivedrab', fontSize=8)
plt.annotate('    ' + str(YTD), xy=(LastDateYTD, LastPrice),
             color='olivedrab', fontSize=8)
plt.legend([SER], loc='upper center', prop={'size': 7})
plt.axhline(round((df3.describe().loc['mean', 'CLOSE']), 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')

LastPrice=abs(df4.CLOSE[-1])
LastDate=str(df4.index[-1])
LastDateYTDs=str(df4.index[0])
LastDateYTD=str(df4.index[12])
LastDateP=str(df4.index[6])
LD=LastDate[:10]
mean=round(df4.describe().loc['mean', 'CLOSE'], 2)
last=df4.describe().loc['count', 'CLOSE']
YTD=round((df4.CLOSE[(int(last)) - 1]
             - df4.CLOSE[0]) / df4.CLOSE[0] * 100, 2)

# plt.subplot(6, 2, 3, facecolor='w')
plt.subplot2grid((6, 2), (5, 1), rowspan=1, colspan=1)
plt.plot(df4.CLOSE, color='coral', linewidth=1)
# plt.xticks([])
plt.yticks([])
plt.axis('on')
plt.annotate("         " + str(df4.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='coral', fontSize=8)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='coral', fontSize=8)
plt.annotate('    %', xy=(LastDateP, LastPrice),
             color='coral', fontSize=8)
plt.annotate('    ' + str(YTD), xy=(LastDateYTD, LastPrice),
             color='coral', fontSize=8)
plt.legend([MIN], loc='upper center', prop={'size': 7})
plt.axhline(round(df4.describe().loc['mean', 'CLOSE'], 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')

LastPrice=abs(df5.CLOSE[-1])
LastDate=str(df5.index[-1])
LastDateYTDs=str(df5.index[0])
LastDateYTD=str(df5.index[12])
LastDateP=str(df5.index[6])
LD=LastDate[:10]
mean=round(df5.describe().loc['mean', 'CLOSE'], 2)
last=df5.describe().loc['count', 'CLOSE']
YTD=round((df5.CLOSE[(int(last)) - 1]
             - df5.CLOSE[0]) / df5.CLOSE[0] * 100, 2)

# plt.subplot(6, 2, 4, facecolor='w')
plt.subplot2grid((6, 2), (3, 1), rowspan=1, colspan=1)
plt.plot(df5.CLOSE, color='cornflowerblue', linewidth=1)
plt.xticks([])
plt.axis('off')
plt.annotate("         " + str(df5.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='cornflowerblue', fontSize=8)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='cornflowerblue', fontSize=8)
plt.annotate('    %', xy=(LastDateP, LastPrice),
             color='cornflowerblue', fontSize=8)
plt.annotate('    ' + str(YTD), xy=(LastDateYTD, LastPrice),
             color='cornflowerblue', fontSize=8)
plt.legend([HOL], loc='upper center', prop={'size': 7})
plt.grid(False)
plt.axhline(round(df5.describe().loc['mean', 'CLOSE'], 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')

LastPrice=abs(df6.CLOSE[-50])
LastDate=str(df6.index[-1])
LastDateYTDs=str(df6.index[0])
LastDateYTD=str(df6.index[12])
LastDateP=str(df6.index[6])
LD=LastDate[:10]
mean=round(df6.describe().loc['mean', 'CLOSE'], 2)
last=df6.describe().loc['count', 'CLOSE']
YTD=round((df6.CLOSE[(int(last)) - 1]
             - df6.CLOSE[0]) / df6.CLOSE[0] * 100, 2)

# plt.subplot(6, 2, 5, facecolor='w')
plt.subplot2grid((6, 2), (1, 1), rowspan=1, colspan=1)
plt.plot(df6.CLOSE, color='darkgoldenrod', linewidth=1)
plt.xticks([])
plt.axis('off')
plt.annotate("         " + str(df6.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='darkgoldenrod', fontSize=8)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='darkgoldenrod', fontSize=8)
plt.annotate('    %', xy=(LastDateP, LastPrice),
             color='darkgoldenrod', fontSize=8)
plt.annotate('    ' + str(YTD), xy=(LastDateYTD, LastPrice),
             color='darkgoldenrod', fontSize=8)
plt.legend([PRO], loc='upper center', prop={'size': 7})
plt.axhline(round(df6.describe().loc['mean', 'CLOSE'], 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')

LastPrice=abs(df7.CLOSE[-1])
LastDate=str(df7.index[-1])
LastDateYTDs=str(df7.index[0])
LastDateYTD=str(df7.index[12])
LastDateP=str(df7.index[6])
LD=LastDate[:10]
mean=round(df7.describe().loc['mean', 'CLOSE'], 2)
last=df7.describe().loc['count', 'CLOSE']
YTD=round((df7.CLOSE[(int(last)) - 1]
             - df7.CLOSE[0]) / df7.CLOSE[0] * 100, 2)

# plt.subplot(6, 2, 6, facecolor='w')
plt.subplot2grid((6, 2), (4, 1), rowspan=1, colspan=1)
plt.plot(df7.CLOSE, color='deepskyblue', linewidth=1)
plt.xticks([])
plt.axis('off')
plt.annotate("         " + str(df7.CLOSE[-1]), xy=(LastDate, LastPrice),
             color='deepskyblue', fontSize=8)
plt.annotate('YTD ', xy=(LastDateYTDs, LastPrice),
             color='deepskyblue', fontSize=8)
plt.annotate('    %', xy=(LastDateP, LastPrice),
             color='deepskyblue', fontSize=8)
plt.annotate('    ' + str(YTD), xy=(LastDateYTD, LastPrice),
             color='deepskyblue', fontSize=8)
plt.legend([FIN], loc='upper center', prop={'size': 7})
plt.axhline(round(df7.describe().loc['mean', 'CLOSE'], 2),
            color='gray', alpha=.4, linewidth=1.2, linestyle='--')


os.chdir(path3)
plt.savefig(end_date + What_Stock + '.png') #, dpi=1200
# plt.tight_layout()
plt.show()
