import os
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime

# --- CONFIGURATION ---
# You can set these via environment variables or edit directly
DATA_DIR = os.environ.get("MAKA_TRADE_DATA_PATH", os.path.abspath(os.path.dirname(__file__)))
CSV_FILENAME = 'conso11292018.csv'  # Update as needed
WHAT_STOCK = 'NOW'
START_DATE = "2018-01-01"
END_DATE = "2018-11-08"
OUTPUT_FILENAME = f'OHLC_{WHAT_STOCK}_{END_DATE}.svg'

# --- FILE LOADING ---
csv_path = os.path.join(DATA_DIR, CSV_FILENAME)
if not os.path.isfile(csv_path):
    raise FileNotFoundError(f"Data file not found: {csv_path}")

df = pd.read_csv(csv_path, index_col=0, parse_dates=True, infer_datetime_format=True)

# --- FILTER DATA ---
df = df[(df.index >= START_DATE) & (df.index <= END_DATE)]
df_stock = df[df['TICKER'] == WHAT_STOCK].copy()

if df_stock.empty:
    raise ValueError(f"No data found for stock {WHAT_STOCK} between {START_DATE} and {END_DATE}")

# --- PREPARE DATA FOR MPLFINANCE ---
df_stock.index.name = 'Date'
ohlc = df_stock[['OPEN', 'HIGH', 'LOW', 'CLOSE']].copy()
ohlc.index = pd.to_datetime(ohlc.index)

# --- PLOT CANDLESTICK CHART ---
mpf_style = mpf.make_mpf_style(base_mpf_style='yahoo', rc={'font.size': 10})
fig, axlist = mpf.plot(
    ohlc,
    type='candle',
    style=mpf_style,
    title=f"{WHAT_STOCK} OHLC ({START_DATE} to {END_DATE})",
    ylabel='Price',
    returnfig=True,
    volume=False,
    figratio=(16, 9),
    figscale=1.2,
    savefig=dict(fname=os.path.join(DATA_DIR, OUTPUT_FILENAME), dpi=120)
)
plt.show()
