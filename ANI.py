#setup modules needed
import pandas as pd
import matplotlib.pyplot as plt

#load csv to a panda dataframe
df = pd.read_csv('PSE Conso.csv')

#To convert Date object to Panda date format
df['DATE'] = pd.to_datetime(df.DATE)

df['DAY'] = df.DATE.dt.weekday_name

#make the dates column as index
df.set_index('DATE', inplace=True)

#new dataframe for the stock $ANI
dfANI = df[df['TICKER']=='ANI']

#Show YTD performance to date
YTD = round((dfANI.CLOSE[137] - dfANI.CLOSE[0]) / dfANI.CLOSE[0], 3) * 100.00
print ('YTD Gain',YTD,'%')

#create a graph of stock price YTD
plt.plot(dfANI.CLOSE)
plt.xlabel('Date')
plt.ylabel('Php Price per Share')
plt.title('ANI YTD 2018 ')
plt.grid(True)
plt.show()


