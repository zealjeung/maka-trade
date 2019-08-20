# setup panda for importing
import pandas as pd
from datetime import datetime
import os
path1 = (r'C:\Users\pdpalmar\Downloads')
path2 = path1
# os.chdir(path2)
# to load latest csv file to a panda dataframe
# input date in the ff. format MMDDYYYY
prevdate = ('05102019')
prevurl = '3970'
end_date = ('05142019')
endurl = '3970'
#i = f'{datetime.now():%m%d%Y}'
#end_date = str(i[:10])
pseurl = str('https://www.pse.com.ph/stockMarket/marketInfo-marketActivity.html?tab=4')
url = str('http://www.stockmarketpilipinas.com/attachment.php?aid='+endurl)
c = pd.read_csv(url)

os.chdir(path1)
c.to_csv('stockQuotes_' + end_date + '.csv')

os.chdir(path1)
latestcsv = 'stockQuotes_' + end_date + '.csv'
dfnew = pd.read_csv(url, names=['TICKER', 'DATE', 'OPEN',
                    'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'NFB'], index_col='DATE')

os.chdir(path2)
# load current conso file
dfconso = pd.read_csv('ytd' + prevdate + '.csv', index_col='DATE')

# to append latest csv to conso file and show stats before and after
dfconso.append(dfnew).to_csv('ytd' + end_date + '.csv')
dfconsoprevdate = pd.read_csv('ytd' + prevdate + '.csv')
print(dfconsoprevdate.tail())
dfconsoenddate = pd.read_csv('ytd' + end_date + '.csv')
print(dfconsoenddate.tail())
print(prevdate, '+', end_date, '=', 'ytd' + end_date + '.csv')
print(len(dfconso), '+', len(dfnew), '=', len(dfconsoenddate))
