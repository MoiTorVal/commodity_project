import pandas as pd 
import os 

os.makedirs("data/merged", exist_ok=True)

# load processed data
gld   = pd.read_csv("data/processed/gld_processed.csv",   parse_dates=["Date"])
dxy   = pd.read_csv("data/processed/dxy_processed.csv",   parse_dates=["Date"])
sp500 = pd.read_csv("data/processed/sp500_processed.csv", parse_dates=["Date"])
tnx   = pd.read_csv("data/processed/tnx_processed.csv",   parse_dates=["Date"])
cpi   = pd.read_csv("data/processed/cpi_processed.csv",   parse_dates=["Date"])

# rename columns so they don't clash during merge
gld   = gld.rename(columns={"Close": "GLD"})
dxy   = dxy.rename(columns={"Close": "DXY"})
sp500 = sp500.rename(columns={"Close": "SP500"})
tnx   = tnx.rename(columns={"Close": "TNX"})

# merge dataframes on Date
df = gld.merge(dxy,  on="Date", how="inner")
df = df.merge(sp500, on="Date", how="inner")
df = df.merge(tnx,  on="Date", how="inner")

# cpi is monthly, so merge with left join to keep all daily data
df = df.merge(cpi, on="Date", how="left")
df["CPI"] = df["CPI"].ffill()  # forward fill CPI values

# calculate inflation rates
df = df.sort_values("Date")
df["Inflation"] = df["CPI"].pct_change(periods=252) * 100 

# calculate real interest rate
df["Real_Rate"] = df["TNX"] - df["Inflation"]

# --- Add Lagged Features ---
df["GLD_Lag30"]  = df["GLD"].shift(30)   # price 30 days ago
df["GLD_Lag60"]  = df["GLD"].shift(60)   # price 60 days ago
df["GLD_Lag90"]  = df["GLD"].shift(90)   # price 90 days ago

# --- Add Rolling Averages ---
df["GLD_MA30"]   = df["GLD"].rolling(window=30).mean()   # 30 day average
df["GLD_MA90"]   = df["GLD"].rolling(window=90).mean()   # 90 day average

# --- Add Momentum ---
df["GLD_Mom30"]  = df["GLD"] - df["GLD"].shift(30)

# drope nulls
df = df.dropna()

# save merged data
df.to_csv("data/processed/final_data.csv", index=False)
print(df.describe())
print(f"\nShape: {df.shape}")