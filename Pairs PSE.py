import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import pprint
# from zipline.api import order_target, record, symbol

Stock1 = 'ATN'
Stock2 = 'ATNB'
end_date = ('11292018')
path2 = (r'D:\Users\jong\PyProjects\Stocks\PSE screener')
os.chdir(path2)
df = pd.read_csv('conso' + end_date + '.csv')
df['DATE'] = pd.to_datetime(df.DATE)
df.set_index('DATE', inplace=True)

"""
dfx = df['TICKER']
dfy = df['TICKER'][1:]

def make_df(dfx, dfy):
    data = {cov: [np.corrcoef + str(i) for i in dfx]
            for i in dfy}
    return pd.DataFrame(data, dfy)

make_df('A', range(3))

for x in df:
    for y in df2['TICKER']:
        #        return pd.df3(x, y)
        print(x)
        print(y)
"""

What_Stock1 = df[df['TICKER'] == Stock1]
What_Stock2 = df[df['TICKER'] == Stock2]

pp = pprint.PrettyPrinter(indent=40, width=41, compact=True, depth=6)
# pp.pprint(What_Stock1.tail(3))
# pp.pprint(What_Stock2.tail(3))

CC = np.corrcoef(What_Stock1['CLOSE'], What_Stock2['CLOSE'])

if np.any(CC > .75):
    pp.pprint(Stock1)
    pp.pprint(Stock2)
    pp.pprint(CC)

fig = plt.figure(figsize=(20, 10))
ax1 = plt.subplot(3, 1, 1, facecolor='w')
What_Stock1['CLOSE'].plot(label='ATN')
What_Stock2['CLOSE'].plot(label='ATNB')
plt.legend()

ax2 = plt.subplot(3, 1, 2, facecolor='w', sharex=ax1)
spread = What_Stock1['CLOSE'] - What_Stock2['CLOSE']
spread.plot(label='Spread', figsize=(20, 10))
plt.axhline(spread.mean(), c='r')
plt.legend()

# 1 day moving average of the price spread
spread_mavg1 = spread.rolling(1).mean()

# 30 day moving average of the price spread
spread_mavg30 = spread.rolling(30).mean()

# Take a rolling 30 day standard deviation
std_30 = spread.rolling(30).std()

# Compute the z score for each day
zscore_30_1 = (spread_mavg1 - spread_mavg30)/std_30

ax3 = plt.subplot(3, 1, 3, facecolor='w', sharex=ax2)
zscore_30_1.plot(label='Rolling 30 day Z score')
plt.axhline(0, color='black')
plt.axhline(1.0, color='red', linestyle='--')
plt.legend()
plt.show()
