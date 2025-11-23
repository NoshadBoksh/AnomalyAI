import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    df = df.copy()
    df["dayofweek"] = df["date"].dt.dayofweek
    df["rolling7"] = df["sales"].rolling(7, min_periods=1).mean()
    X = df[["sales", "dayofweek", "rolling7"]].fillna(0)
    model = IsolationForest(contamination=0.02, random_state=42)
    df["anomaly_score"] = model.fit_predict(X)
    df["anomaly"] = df["anomaly_score"] == -1
    return df, model
