import os
import pandas as pd

# --- CONFIGURATION ---
# Set your data directory here or via environment variable
DATA_DIR = os.environ.get("MAKA_TRADE_DATA_PATH", os.path.abspath(os.path.dirname(__file__)))
PREV_DATE = '11282018'  # Update as needed
END_DATE = '11292018'   # Update as needed
NEW_CSV_FILENAME = 'stockQuotes_' + END_DATE + '.csv'
CONSO_PREV_FILENAME = 'conso' + PREV_DATE + '.csv'
CONSO_NEW_FILENAME = 'conso' + END_DATE + '.csv'

# Path to the new stock quotes CSV
new_csv_path = os.path.join(DATA_DIR, NEW_CSV_FILENAME)
if not os.path.isfile(new_csv_path):
    raise FileNotFoundError(f"Data file not found: {new_csv_path}")

# Path to previous consolidated CSV
conso_prev_path = os.path.join(DATA_DIR, CONSO_PREV_FILENAME)
if not os.path.isfile(conso_prev_path):
    raise FileNotFoundError(f"Data file not found: {conso_prev_path}")

# Read new stock data
dfnew = pd.read_csv(
    new_csv_path,
    names=['TICKER', 'DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'NFB'],
    index_col='DATE'
)

# Read previous consolidated data
dfconso = pd.read_csv(conso_prev_path, index_col='DATE')

# Append new data and write to new consolidated file
df_combined = pd.concat([dfconso, dfnew])
conso_new_path = os.path.join(DATA_DIR, CONSO_NEW_FILENAME)
df_combined.to_csv(conso_new_path)

# Show before and after stats
print("Previous consolidated CSV tail:")
print(dfconso.tail())
print("New stock quotes CSV tail:")
print(dfnew.tail())
print("New consolidated CSV tail:")
print(df_combined.tail())
