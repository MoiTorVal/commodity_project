# Commodity Project — Gold Price Forecasting

This repository contains data processing and modeling code for forecasting gold prices using macro and market indicators.

**Contents**

- `data/processed/final_data.csv` — merged, cleaned dataset used for modeling.
- `src/process_data.py` — scripts to clean raw data.
- `src/merge_data.py` — merges processed series into a single table.
- `src/data_loader.py`, `src/model.py` — data handling and modeling helpers.
- `main.py` — (optional) project runner / experiment entrypoint.

**Setup**

1. Create a Python environment (recommended: venv or conda).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Quick Usage**

- Prepare raw data and run processing:

```bash
python src/process_data.py
python src/merge_data.py
```

- Train or evaluate models (example):

```bash
python src/model.py
```

Adjust scripts and arguments as needed; inspect `src/` for available functions.

**Recommended Next Steps**

- Decide forecast horizon (daily/weekly/monthly) and target (price vs. log-return).
- Run exploratory data analysis on `data/processed/final_data.csv` (missingness, stationarity, correlations, lags).
- Create features (lags, rolling stats, momentum, seasonality) and establish simple baselines.

**Notes**

- The repo's processed data folder is `data/processed/` and the merged table is `final_data.csv`.
- Track experiments externally or add an `experiments/` folder for reproducibility.
