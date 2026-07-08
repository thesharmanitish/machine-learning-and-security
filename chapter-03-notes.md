# Chapter 3 — Anomaly Detection

## Key idea
Detect behavior that deviates from expected baseline, often without reliable labels.

## Techniques covered
- Forecasting (ARIMA, RNN/LSTM-style sequence prediction)
- Statistical detectors (MAD, outlier tests)
- Covariance-based envelope fitting
- Unsupervised detection approaches

## Practical advice
- Build strong features first (host, network, app-level).
- Expect drift; retraining strategy matters.
- Use robust metrics and threshold tuning.
- Prefer interpretable baselines before deep models.
