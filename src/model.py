import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os

os.makedirs("outputs/model", exist_ok=True)

# load data
df = pd.read_csv("data/processed/final_data.csv", parse_dates=["Date"])
df = df.set_index("Date")

# define target
df["Target"] = df["GLD"].pct_change(-30) * 100
df = df.dropna()

# define features 
features = ["DXY", "SP500", "TNX", "CPI", "Inflation", "Real_Rate",
            "GLD_Lag30", "GLD_Lag60", "GLD_Lag90", "GLD_MA30", "GLD_MA90", "GLD_Mom30"]
X = df[features]
y = df["Target"]

# train test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)  

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2 Score: {r2:.4f}")

# plot predictions vs actual
plt.figure(figsize=(12, 5))
plt.plot(y_test.values, label="Actual", color="gold")
plt.plot(predictions, label="Predicted", color="blue", alpha=0.7)
plt.title("Random Forest - Predicted vs Actual GLD Price (30 Days Ahead)")
plt.xlabel("Time")
plt.ylabel("Price (USD)")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/model/predictions_vs_actual.png")
plt.close()
print("Saved predictions_vs_actual.png")

# feature importance
importance = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
plt.figure(figsize=(8, 5))
importance.plot(kind="bar", color="steelblue")
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.savefig("outputs/model/feature_importance.png")
plt.close()
print("Saved feature_importance.png")

print("\nTop Features:")
print(importance)