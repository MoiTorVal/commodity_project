import yfinance as yf
import pandas as pd
import os 
from datetime import datetime

os.makedirs("data/raw", exist_ok=True)

START = "2006-02-01"
END = "2026-02-01"

# --- Yahoo Finance Tickers ---
tickers = {
    "gld_prices": "GLD",        # Gold ETF
    "dxy_prices": "DX-Y.NYB",   # US Dollar Index
    "sp500_prices": "^GSPC",    # S&P 500
    "tnx_prices": "^TNX",       # 10-Year Treasury Yield
}

for filename, ticker in tickers.items():
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start=START, end=END)
    df.to_csv(f"data/raw/{filename}.csv")

# --- FRED Data ---
print("Downloading CPI data from FRED...")
cpi_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL"
cpi = pd.read_csv(cpi_url)
cpi.columns = cpi.columns.str.strip()  # strip any whitespace from column names
cpi = cpi.rename(columns={cpi.columns[0]: "DATE", cpi.columns[1]: "CPIAUCSL"})
cpi["DATE"] = pd.to_datetime(cpi["DATE"])
cpi = cpi.set_index("DATE")
cpi = cpi.loc[START:END]
cpi.to_csv("data/raw/cpi.csv")
print(" Saved to data/raw/cpi_data.csv")

print("\nAll data downloaded successfully.")