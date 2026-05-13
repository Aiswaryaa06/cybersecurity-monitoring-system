import pandas as pd

def save_alerts(alerts):
    df = alerts.reset_index()
    df.columns = ["ip_address", "failed_attempts"]

    df.to_csv("alerts/alerts.csv", index=False)

    print("Alerts saved.")