import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AI Monitoring Dashboard",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 Real-Time AI Monitoring Dashboard")

st.markdown("---")

# Sidebar
st.sidebar.title("MLOps Control Panel")

st.sidebar.success("System Status: ACTIVE")

st.sidebar.info("Model Version: v1.0")

st.sidebar.write("Monitoring Started")

# Top Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Model Accuracy", "78%", "2%")
col2.metric("Predictions", "150", "+20")
col3.metric("Drift Score", "2%", "-1%")
col4.metric("API Status", "Online")

st.markdown("---")

# Monitoring Status
st.subheader("📊 Monitoring Overview")

status_col1, status_col2 = st.columns(2)

with status_col1:
    st.success("✅ Model is running successfully")
    st.success("✅ CI/CD pipeline active")
    st.success("✅ Retraining pipeline healthy")

with status_col2:
    st.info("ℹ️ No significant data drift detected")
    st.info("ℹ️ MLflow tracking enabled")
    st.info("ℹ️ Docker configuration available")

st.markdown("---")

# Fake Prediction Data
st.subheader("📈 Prediction Activity")

data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Predictions": [20, 35, 40, 50, 45, 60, 55]
})

st.line_chart(data.set_index("Day"))

st.markdown("---")

# Drift Monitoring Section
st.subheader("🧠 Data Drift Monitoring")

drift_data = pd.DataFrame({
    "Feature": [
        "MonthlyCharges",
        "tenure",
        "TotalCharges",
        "InternetService"
    ],
    "Drift Status": [
        "No Drift",
        "No Drift",
        "Minor Drift",
        "No Drift"
    ]
})

st.table(drift_data)

st.markdown("---")

# Footer
st.success("🎉 All AI systems operational")
# Dashboard updated