# imports
import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Variables
What_Stock1 = 'MWIDE'
What_Stock2 = '^PSEi'
end_date = ('11292018')
# Paths
path1 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener\stockQuotes')
path2 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener')
path3 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener\stockCaps')
os.chdir(path2)

# Loading
df = pd.read_csv('conso' + end_date + '.csv')
df['DATE'] = pd.to_datetime(df.DATE)
df['DAY'] = df.DATE.dt.weekday_name
df2 = df.sort_values('TICKER')
df2 = df2.set_index('DATE')

AC = df[df['TICKER'] == 'AC']
AC2 = AC.set_index('DATE')
AC2['RETURNS'] = AC2['CLOSE'].pct_change(1)
AC2['Cum Ret'] = (1 + AC2['RETURNS']).cumprod()
AC_ret = AC2['RETURNS']
AC_cumret = AC2['Cum Ret']
AC_close = AC2['CLOSE']

PSEi = df[df['TICKER'] == '^PSEi']
PSEi2 = PSEi.set_index('DATE')
PSEi2['RETURNS'] = PSEi2['CLOSE'].pct_change(1)
PSEi2['Cum Ret'] = (1 + PSEi2['RETURNS']).cumprod()
PSEi_ret = PSEi2['RETURNS']
PSEi_cumret = PSEi2['Cum Ret']
PSEi_close = PSEi2['CLOSE']/8

plt.figure(figsize=(21, 10.8))
plt.subplot(5, 1, 1)
AC_close.plot(label='AC', color='dodgerblue')
PSEi_close.plot(label='PSEi', color='darkorange')
plt.xticks([])
plt.xlabel(' ')
plt.title('Close')
plt.legend()

plt.subplot(5, 1, 2)
#plt.subplot2grid((5, 2), (0, 0), rowspan=2, colspan=1)
plt.bar(AC2.index, AC2.RETURNS, color='dodgerblue', alpha=0.75)
plt.bar(PSEi2.index, PSEi2.RETURNS, color='darkorange', alpha=0.75)
plt.xticks([])
plt.xlabel(' ')
plt.title('Returns')
plt.legend()

plt.subplot(5, 1, 3)
AC_cumret.plot(label='AC', color='dodgerblue')
PSEi_cumret.plot(label='PSEi', color='darkorange')
plt.xlabel(' ')
plt.title('Cumulative Returns')
plt.legend()

plt.subplot(5, 1, 4)
plt.scatter(AC_ret, PSEi_ret, alpha=0.75, color='limegreen')
plt.legend()

plt.subplot(5, 1, 5)
plt.scatter(AC_cumret, PSEi_cumret, alpha=0.75, color='forestgreen')
plt.legend()

plt.grid(False)
plt.tight_layout()
plt.show()
