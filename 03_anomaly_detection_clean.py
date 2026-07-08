import os
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error

dataset = pd.read_csv(os.path.join(os.getcwd(), "datasets", "cpu-a.csv"))
series = dataset["cpu"].astype(float)

split = len(series) - 66
x_train, x_val = series.iloc[:split], series.iloc[split:]

model = sm.tsa.ARIMA(endog=x_train, order=(8, 0, 1))
fit = model.fit()

pred = fit.forecast(steps=len(x_val))
mae = mean_absolute_error(x_val, pred)
print(f"Validation MAE: {mae:.4f}")

plt.figure(figsize=(12, 4))
plt.plot(x_train.index, x_train.values, label="train")
plt.plot(x_val.index, x_val.values, label="true")
plt.plot(x_val.index, pred, label="forecast")
plt.legend()
plt.title("ARIMA Forecast vs True")
plt.show()
