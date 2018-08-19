# Make sure you have run Append.py to update the conso database to latest
# To setup import modules and paths
import datetime
from datetime import datetime
import os
print(os.getcwd())
path1 = (r'C:\Users\...\stock quotes subfolder')
path2 = (r'C:\Users\...\main project folder')

# Choose the stock and last trading date
What_Stock = 'ticker'
# i = f'{datetime.now():%m%d%Y}'
# end_date = str(i[:10])
end_date = ('MMDDYYYY')

# setup modules needed
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-dark')  # other choice: 'seaborn-pastel'

os.chdir(path2)
# load csv to a panda dataframe
df = pd.read_csv('conso' + end_date + '.csv')

# To convert Date object to Panda date format
df['DATE'] = pd.to_datetime(df.DATE)

# to add day of week column
df['DAY'] = df.DATE.dt.weekday_name

# make the dates column as index
df.set_index('DATE', inplace=True)

# new dataframe for the stock $ANI
df2 = df[df['TICKER'] == What_Stock]

last = df2.describe().loc['count', 'CLOSE']
int(last)
YTD = round((df2.CLOSE[(int(last)) - 1] -
             df2.CLOSE[0]) / df2.CLOSE[0], 3) * 100.00

# set index name
df2.index.name = 'DATE'

# creat graph of chosen symbol (1st chart)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(df2.CLOSE)
plt.xlabel('Dates')
plt.ylabel('Daily Closing Prices')
plt.title(What_Stock + ' STOCK PERFORMANCE YTD 2018 ')
plt.grid(True)
plt.legend()

# creat graph of chosen symbol (2nd chart)
plt.subplot(2, 1, 2)
plt.bar(df2.index, df2.VOLUME, color='cyan')
plt.xlabel('Dates')
plt.ylabel('Total Php')
plt.title('DAILY VOLUME')
plt.grid(True)
plt.show()
plt.savefig(end_date + What_Stock + '.png')

# To show the 'AS OF DATE'
print(What_Stock)
print('AS OF DATE:', df2.last_valid_index())

# To show YTD performance to date
print('YTD', YTD, '%')

# to show additional/satistical info
stats = df2.describe()[df2.describe().columns[3:]]
stats.index.name = 'Stats'
print(stats)

