#Only those who has a YTD>20% will graphs be shown

#setup modules needed
import pandas as pd
import matplotlib.pyplot as plt

#load csv to a panda dataframe
df = pd.read_csv('PSE Conso.csv')

#To convert Date object to Panda date format
df['DATE'] = pd.to_datetime(df.DATE)

#to add day of week column
df['DAY'] = df.DATE.dt.weekday_name

#make the dates column as index
df.set_index('DATE', inplace=True)

#choose what stock
#unique = df.TICKER.unique()
#for item in unique:
#   print(item)
What_Stock = 'BDO'

#new dataframe for the stock $ANI
df2 = df[df['TICKER']== What_Stock]

'''
#create a graph of stock price YTD (Unlock this if you want to show all graphs
plt.plot(df2.CLOSE)
plt.xlabel('Dates')
plt.ylabel('Daily Closing Prices')
plt.title( '$' + What_Stock + ' Performance YTD 2018 ')
plt.grid(True)
plt.legend()
plt.show()
'''

#To show 'AS OF DATE'
print(What_Stock)
print('AS OF DATE:', df2.last_valid_index())

last = df2.describe().loc['count', 'CLOSE']
int(last)

#To show YTD performance to date
YTD = round((df2.CLOSE[(int(last))-1] - df2.CLOSE[0]) / df2.CLOSE[0], 3) * 100.00
if (YTD>0):
    print('YTD GAIN:',YTD,'%')
elif (YTD<0):
    print('YTD LOSS:',YTD,'%')
int(YTD)

#to show additional/satistical info
stats = df2.describe()[df2.describe().columns[3:]]
stats.index.name = 'Stats'
print(stats)

if(YTD>20):
    plt.plot(df2.CLOSE)
    plt.xlabel('Dates')
    plt.ylabel('Daily Closing Prices')
    plt.title('$' + What_Stock + ' Performance YTD 2018 ')
    plt.grid(True)
    plt.legend()
    plt.show()
