import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# --- Helper function for Yahoo Finance CSVs ---
def process_yahoo(input_path, output_path):
    df = pd.read_csv(input_path, skiprows=3, parse_dates=[0], names=["Date","Close","High","Low","Open","Volume"])
    df = df[["Date", "Close"]]
    df = df.sort_values("Date")
    df = df.dropna()
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")

# --- Process Yahoo Finance files ---
process_yahoo("data/raw/gld_prices.csv",  "data/processed/gld_processed.csv")
process_yahoo("data/raw/dxy_prices.csv",  "data/processed/dxy_processed.csv")
process_yahoo("data/raw/sp500_prices.csv","data/processed/sp500_processed.csv")
process_yahoo("data/raw/tnx_prices.csv",  "data/processed/tnx_processed.csv")

# --- Process CPI (different structure) ---
cpi = pd.read_csv("data/raw/cpi.csv", parse_dates=["DATE"])
cpi = cpi.rename(columns={"DATE": "Date", "CPIAUCSL": "CPI"})
cpi = cpi.sort_values("Date")
cpi = cpi.dropna()
cpi.to_csv("data/processed/cpi_processed.csv", index=False)
print("Saved to data/processed/cpi_processed.csv")

print("\nAll files processed successfully.")