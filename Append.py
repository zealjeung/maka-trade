#Append needs to be run so that the csv file will be updated to latest trading day.

# setup panda for importing
import pandas as pd
from datetime import datetime
import os

# Edit these paths first
# Where is your csv?
path1 = (r'C:\Users\...)
# Where do you want to save your output file?
path2 = (r'C:\Users\...)
# os.chdir(path2)

# to load from the internet (scraping)
# input date in the ff. format MMDDYYYY
# manually adjust url number (depends on forum thread activity)
prevdate = ('01242019')
prevurl = '3843'
end_date = ('01252019')
endurl = '3844'
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
dfconso = pd.read_csv('conso' + prevdate + '.csv', index_col='DATE')

# to append latest csv to conso file and show stats before and after
dfconso.append(dfnew).to_csv('conso' + end_date + '.csv')
dfconsoprevdate = pd.read_csv('conso' + prevdate + '.csv')
print(dfconsoprevdate.tail())
dfconsoenddate = pd.read_csv('conso' + end_date + '.csv')
print(dfconsoenddate.tail())
print(prevdate, '+', end_date, '=', 'conso' + end_date + '.csv')
print(len(dfconso), '+', len(dfnew), '=', len(dfconsoenddate))
