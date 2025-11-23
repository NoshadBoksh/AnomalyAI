import pandas as pd
import numpy as np

np.random.seed(0)
days = pd.date_range("2025-01-01", periods=180, freq="D")
base = 200 + np.cumsum(np.random.normal(loc=0.2, scale=3, size=len(days)))
noise = np.random.normal(0, 10, size=len(days))
sales = np.maximum(0, base + noise)
sales[[20, 95, 150]] = sales[[20, 95, 150]] * np.array([3.5, 0.2, 4.0])

df = pd.DataFrame({"date": days, "sales": sales})
df.to_csv("data/example_sales.csv", index=False)
print("Saved data/example_sales.csv")
