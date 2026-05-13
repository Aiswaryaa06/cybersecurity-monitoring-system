import streamlit as st
import pandas as pd
import sys
import os
import time
import plotly.express as px

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.data_generator import generate_logs
from detector import (
    detect_failed_logins,
    calculate_risk_scores,
    save_incidents
)

# -------------------------
# UI THEME
# -------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #0f172a, #111827);
        color: white;
    }

    h1, h2, h3 {
        color: #38bdf8;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    div[data-testid="metric-container"] {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 15px;
    }

    .stDataFrame {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🕵🏻‍♂️ Log Monitoring and Intrusion Detection System")

# -------------------------
# LOAD DATA
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(BASE_DIR, "data", "logs.csv")

logs = pd.read_csv(csv_path)

# 🔥 FIX 1: timestamp cleanup + spread (IMPORTANT CORE FIX)
logs["timestamp"] = pd.to_datetime(logs["timestamp"], errors="coerce")

if len(logs) > 0:
    logs = logs.sort_values("timestamp").reset_index(drop=True)
    logs["timestamp"] = logs["timestamp"] + pd.to_timedelta(logs.index * 2, unit="s")

ip_col = "ip_address" if "ip_address" in logs.columns else "ip"

# -------------------------
# SIDEBAR FILTERS
# -------------------------
st.sidebar.title("🔍 Filters")

users = ["All"] + sorted(logs["username"].unique().tolist())
selected_user = st.sidebar.selectbox("Select User", users)

ips = ["All"] + sorted(logs[ip_col].unique().tolist())
selected_ip = st.sidebar.selectbox("Select IP Address", ips)

time_filter = st.sidebar.selectbox(
    "Time Filter",
    ["All Time", "Last 1 Hour", "Last 24 Hours"]
)

# -------------------------
# APPLY FILTERS
# -------------------------
filtered_logs = logs.copy()

if selected_user != "All":
    filtered_logs = filtered_logs[filtered_logs["username"] == selected_user]

if selected_ip != "All":
    filtered_logs = filtered_logs[filtered_logs[ip_col] == selected_ip]

now = pd.Timestamp.now()

if time_filter == "Last 1 Hour":
    filtered_logs = filtered_logs[filtered_logs["timestamp"] >= now - pd.Timedelta(hours=1)]

elif time_filter == "Last 24 Hours":
    filtered_logs = filtered_logs[filtered_logs["timestamp"] >= now - pd.Timedelta(hours=24)]

# -------------------------
# METRICS
# -------------------------
failed_count = len(filtered_logs[filtered_logs["status"] == "FAILED"])
success_count = len(filtered_logs[filtered_logs["status"] == "SUCCESS"])
total_logs = len(filtered_logs)
unique_ips = filtered_logs[ip_col].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("📄 Total Logs", total_logs)
col2.metric("❌ Failed Logins", failed_count)
col3.metric("✅ Successful Logins", success_count)
col4.metric("🌐 Unique IPs", unique_ips)

# -------------------------
# LOG TABLE
# -------------------------
st.subheader("📄 Filtered Logs")
st.dataframe(filtered_logs)

# -------------------------
# DETECTION ENGINE
# -------------------------
st.markdown("## 🚨 Intrusion Detection System")

suspicious_ips = detect_failed_logins(filtered_logs)

if not suspicious_ips.empty:
    st.error("🚨 CRITICAL ALERT: Possible brute force attack detected!")

    for ip, count in suspicious_ips.items():
        st.warning(f"⚠️ {ip} → {count} failed attempts")

    save_incidents(filtered_logs)
else:
    st.success("🟢 No active threats detected")

# -------------------------
# ATTACK TIMELINE (FIXED CORE)
# -------------------------
st.markdown("## ⏱ Attack Timeline (Failed Login Burst Detection)")

failed_logs = filtered_logs[filtered_logs["status"] == "FAILED"].copy()

# STEP 1: clean timestamps
failed_logs["timestamp"] = pd.to_datetime(failed_logs["timestamp"], errors="coerce")
failed_logs = failed_logs.dropna(subset=["timestamp"])

# STEP 2: FORCE SORT
failed_logs = failed_logs.sort_values("timestamp")

if not failed_logs.empty:

    # STEP 3: IMPORTANT FIX → normalize to MINUTE LEVEL FIRST
    failed_logs["time_bucket"] = failed_logs["timestamp"].dt.floor("min")

    timeline = failed_logs.groupby("time_bucket").size()

    # STEP 4: fill missing time gaps (CRITICAL FIX)
    full_range = pd.date_range(
        start=timeline.index.min(),
        end=timeline.index.max(),
        freq="min"
    )

    timeline = timeline.reindex(full_range, fill_value=0)

    # STEP 5: plot
    st.line_chart(timeline)

    # STEP 6: smarter burst detection
    if timeline.rolling(3).sum().max() >= 5:
        st.error("🚨 BRUTE FORCE ATTACK BURST DETECTED")

else:
    st.info("No failed login data available for timeline.")
# -------------------------
# GEO ATTACK MAP
# -------------------------
st.markdown("## 🌍 World Attack Heatmap")

if not failed_logs.empty:

    country_counts = failed_logs["country"].value_counts().reset_index()
    country_counts.columns = ["country", "count"]

    fig = px.choropleth(
        country_counts,
        locations="country",
        locationmode="country names",
        color="count",
        color_continuous_scale="Reds"
    )

    st.plotly_chart(fig)

else:
    st.info("No geo attack data available.")

# -------------------------
# RISK SCORING
# -------------------------
st.markdown("## 🧠 Threat Risk Scoring")

risk_df = calculate_risk_scores(filtered_logs)

if not risk_df.empty:
    st.dataframe(risk_df)

    high_risk = risk_df[risk_df["Severity"] == "HIGH"]

    if not high_risk.empty:
        st.error("🚨 HIGH RISK THREATS DETECTED")
else:
    st.success("No suspicious activity found")

# -------------------------
# INCIDENT HISTORY
# -------------------------
st.markdown("## 🧾 Incident History Log")

incident_path = os.path.join(BASE_DIR, "data", "incidents.csv")

if os.path.exists(incident_path):
    incident_logs = pd.read_csv(incident_path)
    st.dataframe(incident_logs)

    csv = incident_logs.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Incident History",
        data=csv,
        file_name="incident_history.csv",
        mime="text/csv"
    )
else:
    st.info("No incidents recorded yet.")

# -------------------------
# DOWNLOAD REPORT
# -------------------------
st.subheader("📁 Download Incident Report")

csv = filtered_logs.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Report (CSV)",
    data=csv,
    file_name="incident_report.csv",
    mime="text/csv"
)

# -------------------------
# LIVE SIMULATION (FIXED CORE LOOP)
# -------------------------
st.subheader("Live Simulated Logs")

placeholder = st.empty()

if st.button("Start Live Feed"):

    for i in range(10):

        live_logs = generate_logs(50)

        # 🔥 FIX: force time progression (critical SOC behavior)
        live_logs["timestamp"] = pd.to_datetime(live_logs["timestamp"], errors="coerce")
        live_logs["timestamp"] = live_logs["timestamp"] + pd.to_timedelta(i * 5, unit="s")

        with placeholder.container():
            st.dataframe(live_logs)

        time.sleep(2)