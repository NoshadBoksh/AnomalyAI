import streamlit as st
import pandas as pd
from src.model import detect_anomalies

st.title("AnomalyAI")

uploaded = st.file_uploader("Upload CSV with date and sales columns", type="csv")

if uploaded:
    df = pd.read_csv(uploaded, parse_dates=["date"])
    result, _ = detect_anomalies(df)
    st.write("Anomalies found:")
    st.dataframe(result[result["anomaly"]])
    st.line_chart(result.set_index("date")["sales"])
