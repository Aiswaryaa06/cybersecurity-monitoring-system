import pandas as pd
import os
def detect_failed_logins(df, threshold=3):
    suspicious = df[df["status"] == "FAILED"]

    # auto-detect correct column
    ip_col = "ip_address" if "ip_address" in df.columns else "ip"

    grouped = suspicious.groupby(ip_col).size()

    return grouped[grouped >= threshold]

#RISK SCORING SYSTEM
# -------------------------
def calculate_risk_scores(df):

    ip_col = "ip_address" if "ip_address" in df.columns else "ip"

    failed = df[df["status"] == "FAILED"]

    ip_counts = failed.groupby(ip_col).size()

    risk_data = []

    for ip, count in ip_counts.items():

        # Risk score logic
        score = count * 20

        if score > 100:
            score = 100

        # Severity classification
        if score >= 80:
            severity = "HIGH"
        elif score >= 50:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        risk_data.append({
            "IP Address": ip,
            "Failed Attempts": count,
            "Risk Score": score,
            "Severity": severity
        })

    return pd.DataFrame(risk_data)

def save_incidents(df, file_path="data/incidents.csv"):

    ip_col = "ip_address" if "ip_address" in df.columns else "ip"

    failed = df[df["status"] == "FAILED"]

    grouped = failed.groupby(ip_col).size()

    incidents = grouped[grouped >= 3].reset_index()
    incidents.columns = ["IP Address", "Failed Attempts"]

    # add metadata
    incidents["Severity"] = incidents["Failed Attempts"].apply(
        lambda x: "HIGH" if x >= 6 else "MEDIUM"
    )

    incidents["Timestamp"] = pd.Timestamp.now()

    # create file if not exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    if os.path.exists(file_path):
        old = pd.read_csv(file_path)
        combined = pd.concat([old, incidents], ignore_index=True)
    else:
        combined = incidents

    combined.to_csv(file_path, index=False)

    return combined