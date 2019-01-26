# maka-trade
Learning python for algorhythmic trading and data science(analysis/visualization)

I initially learn how to get PSE daily stock data thru a software called 'PSE Get' ->ctto https://www.facebook.com/pseget/ which converts the daily PDF to daily csv files.
I was able to get an Excel add-on from a friend that appends multiple sheets into one. Hence, the ...conso.csv file.
I learned how to manipulate data into a data frame with proper indexing that will allow plotting using pd and plt.
I computed the YTD gain of the stock and other statistics.

ToDos/Next Steps:
>I'll automate appending of the files into python thru web scraping a forum thread in stockmarketpilipinas.com since PSE Get no longer works.
>I would like to have a filtering program such that I'll get a list of stocks that are in the Stage 2 market cycle or those that are clearly advancing in price.

Before:
>As an improvement I'll convert the line graph into a legit OHLC/Candlestick chart ... or even animated SVG(if that possible).
>Probably next I will include volume data into the chart and pull-off a Minervini VCP strategy/setup.

Latest:
Ill stick with the line plot but now I already have the featured stock, the main index PSEI, volume, net foreign, and Sectors in one dashboard, which I often upload in Investagrams. I run the Append.py and ScreenerSectors.py
